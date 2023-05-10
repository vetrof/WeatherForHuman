import requests


def get_kp_index_current(forecast_w):
    link = "https://services.swpc.noaa.gov/products/noaa-planetary-k-index.json"
    api_resp_sw = requests.get(link).json()
    l = len(api_resp_sw) - 1

    # k_index_current = {'kp_index': float(api_resp_sw[l][1])}
    # return dict['current']['kp_index'] = api_resp_sw[l][1]

    forecast_w['current']['k_index_current'] = api_resp_sw[l][1]

    return forecast_w
