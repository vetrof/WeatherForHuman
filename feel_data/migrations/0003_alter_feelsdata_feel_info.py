# Generated by Django 4.2 on 2023-04-10 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feel_data', '0002_alter_feelsdata_feel_num_alter_feelsdata_hum_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feelsdata',
            name='feel_info',
            field=models.TextField(blank=True, null=True, verbose_name='самочувствие подробно'),
        ),
    ]
