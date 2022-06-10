from django.urls import path

from .views import *

urlpatterns = [
path('stat/', StatsView.as_view(), name="stats"),

]