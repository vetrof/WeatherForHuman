from all_requests.models import AllRequest
from feel_data.models import FeelsData


def save_feel(request, feel_num, feel_info='none'):
    user_requests = AllRequest.objects.filter(user=request.user)
    last_user_requests = user_requests.last()

    user = request.user
    feel_num = feel_num
    feel_info = feel_info

    location = last_user_requests.location
    temp_c = last_user_requests.temp_c
    temp_c_feel = last_user_requests.temp_c_feel
    hum = last_user_requests.hum
    wind = last_user_requests.wind
    wind_gust = last_user_requests.wind_gust
    pressure_mm = last_user_requests.pressure_mm
    k_index = last_user_requests.k_index

    FeelsData.objects.create(user=user,
                             feel_num=feel_num,
                             feel_info=feel_info,
                             location=location,
                             temp_c=temp_c,
                             temp_c_feel=temp_c_feel,
                             hum=hum,
                             wind=wind,
                             wind_gust=wind_gust,
                             pressure_mm=pressure_mm,
                             k_index=k_index)
