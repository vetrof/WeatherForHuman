from rest_framework.serializers import ModelSerializer

from feel_data.models import FeelsData


class CurrenWeatherSerializer(ModelSerializer):

    class Meta:
        model = FeelsData
        fields = ['user', 'location', 'create_at']
