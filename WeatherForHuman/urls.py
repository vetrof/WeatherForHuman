
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.urls import path

from checklocation.views import check_location
from feel_data.views import save_feel_data
from getlocation.views import get_location
from getweather.views import get_current_weather, get_forecast_weather, \
    weather_api
from index_view.views import index_view
from login.views import LoginUserView
from my_feel_history.views import FeelHistoryView
from registration.views import UserRegistrationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),

    path('', index_view, name='index'),
    path('get_location/', get_location, name='get_location'),
    path('check_location/', check_location, name='check_location'),

    path('get_weather/<str:loc>', get_current_weather, name='get_weather'),
    path('get_forecast/1/<str:loc>', get_forecast_weather,
         name='get_forecast_1'),

    path('save_feel_data/', save_feel_data, name='save_feel_data'),
    path('feel_history/', login_required(FeelHistoryView.as_view()),
         name='feel_history'),

    # api
    path('api/<str:loc>', weather_api),

]

