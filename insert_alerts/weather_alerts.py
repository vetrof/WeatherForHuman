WIND_RED = 35
WIND_YELLOW = 25

GUST_RED = 35
GUST_YELLOW = 25

PRESSURE_HIGH_RED = 770
PRESSURE_HIGH_YELLOW = 765
PRESSURE_NEUTRAL = 760
PRESSURE_LOW_YELLOW = 755
PRESSURE_LOW_RED = 750

K_RED_ZONE = 5
K_YELLOW_ZONE = 3


def insert_weather_alerts(forecast_w):
    # insert current alerts

    current_wind = forecast_w['current']['wind_kph']
    current_gust = forecast_w['current']['gust_kph']
    current_pressure = forecast_w['current']['pressure_mm']
    current_k_index = float(forecast_w['current']['k_index_current'])

    if current_wind > WIND_RED:
        forecast_w['current']['wind_alert'] = 'red'
    elif current_wind > WIND_YELLOW:
        forecast_w['current']['wind_alert'] = 'orange'

    if current_gust > GUST_RED:
        forecast_w['current']['gust_alert'] = 'red'
    elif current_gust > GUST_YELLOW:
        forecast_w['current']['gust_alert'] = 'orange'

    if current_pressure > PRESSURE_HIGH_RED or current_pressure < PRESSURE_LOW_RED:
        forecast_w['current']['pressure_alert'] = 'red'
    elif current_pressure > PRESSURE_HIGH_YELLOW or current_pressure < PRESSURE_LOW_YELLOW:
        forecast_w['current']['pressure_alert'] = 'orange'

    if current_k_index > K_RED_ZONE:
        forecast_w['current']['k_index_alert'] = 'red'
    elif current_k_index > K_YELLOW_ZONE:
        forecast_w['current']['k_index_alert'] = 'orange'

    # insert forecast alerts

    days = len(forecast_w['forecast']['forecastday'])

    for day in range(days):

        hour_forecast = forecast_w['forecast']['forecastday'][day]['hour']
        time = 0
        for hour in hour_forecast:

            wind_speed = hour['wind_kph']
            gust = hour['gust_kph']
            pressure = hour['mm_pressure']
            k_index = 0

            try:
                k_index = float(hour['k_index'])

            except:
                k_index = 0

            if wind_speed > WIND_RED:
                forecast_w['forecast']['forecastday'][day]['hour'][time][
                    'wind_alert'] = 'red'
            elif wind_speed > WIND_YELLOW:
                forecast_w['forecast']['forecastday'][day]['hour'][time][
                    'wind_alert'] = 'orange'

            # wind speed alert
            if gust > GUST_RED:
                forecast_w['forecast']['forecastday'][day]['hour'][time][
                    'gust_alert'] = 'red'
            elif gust > GUST_YELLOW:
                forecast_w['forecast']['forecastday'][day]['hour'][time][
                    'gust_alert'] = 'orange'

            # pressure  alert
            if pressure > PRESSURE_HIGH_RED or pressure < PRESSURE_LOW_RED:
                forecast_w['forecast']['forecastday'][day]['hour'][time][
                    'pressure_alert'] = 'red'
            elif pressure > PRESSURE_HIGH_YELLOW or pressure < PRESSURE_LOW_YELLOW:
                forecast_w['forecast']['forecastday'][day]['hour'][time][
                    'pressure_alert'] = 'orange'

            # k index  alert
            if k_index > K_RED_ZONE:
                forecast_w['forecast']['forecastday'][day]['hour'][time][
                    'k_index_alert'] = 'red'
            elif k_index > K_YELLOW_ZONE:
                forecast_w['forecast']['forecastday'][day]['hour'][time][
                    'k_index_alert'] = 'orange'

            time += 1

    return forecast_w
