
from django.contrib import admin
from django.urls import path, include

from Userapp.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(), name='home'),
    path('stats/', include('Statsapp.urls')),
    path('user/', include('Userapp.urls')),
    path('asosiy/', include('Asosiyapp.urls')),
]
