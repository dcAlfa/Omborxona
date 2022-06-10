from django.urls import path

from .views import *

urlpatterns = [
path("bolim/", BolimView.as_view(), name="bolim"),
path("client/", ClientView.as_view(), name="client"),
path("client_up/", Client_UpView.as_view(), name="client_up"),
path("pro/", ProView.as_view(), name="pro"),
path("pro_up/", Pro_UpView.as_view(), name="pro_up"),
]