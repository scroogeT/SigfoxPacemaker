from django.urls import path
from django.contrib.auth.decorators import login_required

from dashboard import views

app_name = 'dashboard'

urlpatterns = [
    path('', login_required(views.Home.as_view(), login_url='/accounts/login/'), name='home'),
    path('device-info/<int:pk>/', login_required(views.DeviceInfo.as_view(), login_url='/accounts/login/'), name='device_info'),
    path('devices/', views.DeviceList.as_view()),
    path('device-readings/', views.DeviceReadings.as_view()),
    path('sigfox-message/', views.SigfoxMessage.as_view())
]
