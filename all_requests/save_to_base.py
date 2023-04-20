from all_requests.models import AllRequest


def save_to_base(data, user=None):
    # save data in base

    location = data['location']['name']
    temp_c = data['current']['temp_c']
    temp_c_feel = data['current']['feelslike_c']
    hum = data['current']['humidity']
    wind = data['current']['wind_kph']
    wind_gust = data['current']['gust_kph']
    pressure_mm = data['current']['pressure_mm']
    k_index = data['current']['k_index_current']

    AllRequest.objects.create(user=user,
                              location=location,
                              temp_c=temp_c,
                              temp_c_feel=temp_c_feel,
                              hum=hum,
                              wind=wind,
                              wind_gust=wind_gust,
                              pressure_mm=pressure_mm,
                              k_index=k_index)
