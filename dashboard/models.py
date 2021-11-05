from django.db import models
from django.urls import reverse


class Device(models.Model):
    number = models.CharField(max_length=30, unique=True)
    added_on = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('dashboard:device_info', args=[str(self.id)])


class DeviceReading(models.Model):
    MESSAGE_TYPE = (
        ('READING', 'Reading'),
        ('TAMPER', 'Tamper')
    )
    device = models.ForeignKey(Device, related_name='readings', on_delete=models.CASCADE)
    message_type = models.CharField(max_length=30, choices=MESSAGE_TYPE)
    reading = models.FloatField()
    device_voltage = models.FloatField()
    seq_number = models.PositiveIntegerField(unique=True)
    recorded_on = models.DateTimeField()
    # TODO: RECORD ALL META INFO FIELDS LIKE LOCATION ETC
    added_on = models.DateTimeField(auto_now_add=True)
