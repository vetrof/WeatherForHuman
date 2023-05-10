from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
import requests

from WeatherForHuman import settings
from WeatherForHuman.settings import weather_api_key


def check_location(request):
    loc = request.GET.get('loc')
    # status = True
    loc_info = {}

    search_link = (f'http://api.weatherapi.com/v1/'
                   f'search.json?key={weather_api_key}&q={loc}')

    api_resp_w = requests.get(search_link).json()

    if api_resp_w:
        status = True
        loc_info = api_resp_w[0]
        true_link = f"{settings.DOMAIN_NAME}/get_forecast/1/{loc}"
        return HttpResponseRedirect(true_link)

    else:
        status = False
        messages.success(request,
                         'Такого города нет в базе, попробуйте еще раз.')
        return HttpResponseRedirect(request.META['HTTP_REFERER'])





