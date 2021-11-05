from rest_framework import serializers
from dashboard import models


class SigfoxMessageSerializer(serializers.Serializer):
    device = serializers.CharField(max_length=30)
    time = serializers.CharField(max_length=20)
    snr = serializers.CharField(max_length=20)
    station = serializers.CharField(max_length=20)
    data = serializers.CharField(max_length=20)
    avgSnr = serializers.CharField(max_length=20)
    lat = serializers.CharField(max_length=20)
    lng = serializers.CharField(max_length=20)
    rssi = serializers.CharField(max_length=20)
    seqNumber = serializers.CharField(max_length=20)


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Device
        fields = '__all__'


class DeviceReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DeviceReading
        fields = '__all__'
