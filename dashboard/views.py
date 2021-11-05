from datetime import datetime

from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.views import APIView, Response
from dashboard import models, serializers
from django.views import generic
from django.contrib.auth.decorators import login_required


# @login_required
class Home(generic.ListView):
    model = models.Device
    context_object_name = 'devices'
    template_name = 'dashboard/index.html'
    queryset = models.Device.objects.all()


class DeviceInfo(generic.DetailView):
    model = models.Device
    template_name = 'dashboard/deviceInfo.html'
    queryset = models.Device.objects.all()

    def get_context_data(self, **kwargs):
        context = super(DeviceInfo, self).get_context_data(**kwargs)
        readings = models.DeviceReading.objects.filter(device=context.get('device'))

        context['readings'] = readings

        return context


class DeviceList(generics.ListAPIView):
    """
        List All the devices in the database
    """
    serializer_class = serializers.DeviceSerializer
    queryset = models.Device.objects.all()


class DeviceReadings(generics.ListAPIView):
    """
        View all the device readings received
    """
    serializer_class = serializers.DeviceReadingSerializer
    queryset = models.DeviceReading.objects.all()


class SigfoxMessage(APIView):
    """
        Public endpoint to receive all Sigfox downlink messages.
        Send a fully formed Sigfox message to save device readings
    """
    @swagger_auto_schema(request_body=serializers.SigfoxMessageSerializer)
    def post(self, request):
        payload = request.data

        device, _ = models.Device.objects.get_or_create(number=payload.get('device'))

        snapshot_time = datetime.fromtimestamp(int(payload.get('time')))
        reading = int(payload.get('data')[:2], 16)

        if payload.get('data')[2:]:
            voltage = int(payload.get('data')[2:], 16) * 0.001
        else:
            voltage = 0

        seq_number = int(payload.get('seqNumber'))

        if reading == 1:
            message_type = 'TAMPER'
        else:
            message_type = 'READING'

        device_reading, _ = models.DeviceReading.objects.get_or_create(
            device=device, device_voltage=voltage, reading=reading,
            message_type=message_type, seq_number=seq_number, recorded_on=snapshot_time)

        return Response(status=status.HTTP_200_OK)
