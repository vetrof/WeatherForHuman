from django.db import models
from django.db.models import PROTECT

from users.models import User


class FeelsData(models.Model):

    user = models.ForeignKey(to=User, on_delete=PROTECT)
    feel_num = models.FloatField('самочувствие')
    feel_info = models.TextField('самочувствие подробно', blank=True, null=True)

    location = models.CharField('город', max_length=250,)
    create_at = models.DateTimeField(auto_now_add=True, null=True,
                                     blank=True)

    temp_c = models.FloatField('temp_c')
    temp_c_feel = models.FloatField('temp_c_feel')
    hum = models.FloatField('hum')
    wind = models.FloatField('wind')
    wind_gust = models.FloatField('wind_gust')
    pressure_mm = models.FloatField('pressure_mm')
    k_index = models.FloatField('k_index')


    def __str__(self):
        return f'{self.id} {self.user} | {self.location} | {self.feel_num}'
