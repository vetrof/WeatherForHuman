import requests
from datetime import timedelta, date


def get_k_index_forecast(forecast_w):
    localtime = forecast_w['location']['localtime']
    localtime = localtime.split()
    localtime = localtime[0].split('-')

    year = localtime[0]
    month = localtime[1]
    day = localtime[2]

    k_index_forecast = {}
    k_index_forecast0 = {}
    k_index_forecast1 = {}
    k_index_forecast2 = {}

    now = date(year=int(year), month=int(month), day=int(day))

    now_0 = str(now)
    now_1 = str(now + timedelta(days=1))
    now_2 = str(now + timedelta(days=2))

    url = f'https://services.swpc.noaa.gov/products/' \
          f'noaa-planetary-k-index-forecast.json'
    response = requests.get(url)
    data = response.json()


    start_time = 0
    for i in data:
        if now_0 in i[0]:
            k_index_forecast0[f'{start_time}'] = i[1]
            forecast_w['forecast']['forecastday'][0]['hour'][start_time]['k_index'] = i[1]
            # print(now, now_0, i)
            start_time += 3

    start_time = 0
    for i in data:
        if now_1 in i[0]:
            k_index_forecast1[f'{start_time}'] = i[1]
            forecast_w['forecast']['forecastday'][1]['hour'][start_time][
                'k_index'] = i[1]
            start_time += 3

    start_time = 0
    for i in data:
        if now_2 in i[0]:
            k_index_forecast2[f'{start_time}'] = i[1]
            # forecast_w['forecast']['forecastday'][2]['hour'][start_time][
            #     'k_index'] = i[1]
            start_time += 3

    k_index_forecast[0] = k_index_forecast0
    k_index_forecast[1] = k_index_forecast1
    k_index_forecast[2] = k_index_forecast2

    return forecast_w, k_index_forecast
