# Generated by Django 4.2 on 2023-04-10 15:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AllRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=250, verbose_name='город')),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('temp_c', models.FloatField(verbose_name='temp_c')),
                ('temp_c_feel', models.FloatField(verbose_name='temp_c_feel')),
                ('hum', models.FloatField(verbose_name='hum')),
                ('wind', models.FloatField(verbose_name='wind')),
                ('wind_gust', models.FloatField(verbose_name='wind_gust')),
                ('pressure_mm', models.FloatField(verbose_name='pressure_mm')),
                ('k_index', models.FloatField(verbose_name='k_index')),
                ('user', models.ForeignKey(default='не указан', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]