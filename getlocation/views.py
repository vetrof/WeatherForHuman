from django.shortcuts import render
import requests
from WeatherForHuman.settings import IPINFO_KEY, OPEN_CA_DATA_KEY


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_location(request):
    ip = get_client_ip(request)

    # Отправляем запрос к API для определения города по IP
    api_key = 'b4c1625c91da62'
    response = requests.get(f'https://ipinfo.io/{ip}?token={IPINFO_KEY}')
    data = response.json()

    city = data.get('city', 'Unknown')  # Получаем название города или "Unknown", если не удалось определить

    return render(request, 'getlocation/get_location.html', {'ip': ip, 'city': city, 'OPEN_CA_DATA_KEY': OPEN_CA_DATA_KEY})
