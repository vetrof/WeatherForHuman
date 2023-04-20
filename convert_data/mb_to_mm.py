RATE = 0.75


def get_pressure_in_mm(forecast_w):
    hour_forecast0 = forecast_w['forecast']['forecastday'][0]['hour']
    hour_forecast1 = forecast_w['forecast']['forecastday'][1]['hour']

    current_pressure_mb = forecast_w['current']['pressure_mb']
    current_pressure_mm = current_pressure_mb * 0.75
    forecast_w['current']['pressure_mm'] = current_pressure_mm

    # insert pressure mm for today forecast
    time = 0
    for hour in hour_forecast0:
        mb_pressure = hour['pressure_mb']

        forecast_w['forecast']['forecastday'][0]['hour'][time][
            'mm_pressure'] = mb_pressure * RATE

        time += 1

    # insert pressure mm for tomorrow forecast
    time = 0
    for hour in hour_forecast1:
        mb_pressure = hour['pressure_mb']

        forecast_w['forecast']['forecastday'][1]['hour'][time][
            'mm_pressure'] = mb_pressure * RATE

        time += 1

    return forecast_w
