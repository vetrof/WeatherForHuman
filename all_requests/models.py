from django.db import models
from django.db.models import PROTECT

from users.models import User


class AllRequest(models.Model):
    user = models.ForeignKey(to=User, on_delete=PROTECT, null=True, blank=True)

    location = models.CharField('город', max_length=250, )
    create_at = models.DateTimeField(auto_now_add=True, null=True,
                                     blank=True)

    temp_c = models.FloatField('temp_c')
    temp_c_feel = models.FloatField('temp_c_feel')
    hum = models.FloatField('hum')
    wind = models.FloatField('wind')
    wind_gust = models.FloatField('wind_gust')
    pressure_mm = models.FloatField('pressure_mm')
    k_index = models.FloatField('k_index')


