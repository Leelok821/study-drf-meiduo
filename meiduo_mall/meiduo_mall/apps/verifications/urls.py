from django.urls import path
from verifications import views

urlpatterns = [
    path('sms_codes/<int:mobile>/', views.SmsCodeVeiw.as_view())
]