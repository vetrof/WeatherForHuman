import requests
import json
from django.http import HttpResponse
from django.shortcuts import render

from WeatherForHuman.settings import weather_api_key

from all_requests.save_to_base import save_to_base
from convert_data.mb_to_mm import get_pressure_in_mm

from get_k_index.get_current_k_index import get_kp_index_current
from get_k_index.get_k_index_forecast import get_k_index_forecast


from insert_alerts.weather_alerts import insert_weather_alerts
from users.models import User


def get_current_weather(request, loc):
    # current weather
    api_answer_cur = f'http://api.weatherapi.com/v1/' \
                 f'current.json?key={weather_api_key}&q={loc}&aqi=no'
    current_w = requests.get(api_answer_cur).json()
    return render(request, 'getweather/getweather.html', current_w)


def get_forecast_weather(request, loc):
    forecast_w = {}

    if loc == 'None':
        forecast_w['status'] = 'None'
        return render(request, 'getweather/get_forecast_1day.html', forecast_w)

    else:
        api_answer_for = f'http://api.weatherapi.com/v1/' \
                         f'forecast.json?key={weather_api_key}' \
                         f'&q={loc}&days=2&aqi=no&alerts=yes'
        forecast_w = requests.get(api_answer_for).json()

        # add to data kp index current and forecast
        forecast_w = get_kp_index_current(forecast_w)
        forecast_w, k_index_forecast = get_k_index_forecast(forecast_w)

        # add to data pressure in mm
        forecast_w = get_pressure_in_mm(forecast_w)

        # add color alerts
        forecast_w = insert_weather_alerts(forecast_w)

        # save data in base

        if request.user.username:
            user = request.user
        else:
            user = None

        save_to_base(forecast_w, user)

        return render(request, 'getweather/get_forecast_1day.html', forecast_w)


def weather_api(request, loc):
    forecast_w = {}

    if loc == 'None':
        forecast_w['status'] = 'None'
        return render(request, 'getweather/get_forecast_1day.html', forecast_w)

    else:
        api_answer_for = f'http://api.weatherapi.com/v1/' \
                         f'forecast.json?key={weather_api_key}' \
                         f'&q={loc}&days=2&aqi=no&alerts=yes'
        forecast_w = requests.get(api_answer_for).json()

        # add to data kp index current and forecast
        forecast_w = get_kp_index_current(forecast_w)
        forecast_w, k_index_forecast = get_k_index_forecast(forecast_w)

        # add to data pressure in mm
        forecast_w = get_pressure_in_mm(forecast_w)

        # add color alerts
        forecast_w = insert_weather_alerts(forecast_w)

        # save data in base

        if request.user.username:
            user = request.user
        else:
            user = None

        save_to_base(forecast_w, user)

        json_data = json.dumps(forecast_w)

    return HttpResponse(json_data, content_type='application/json')
