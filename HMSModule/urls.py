from django.contrib import admin
from django.urls import include,path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('Patient/', include('Patient.urls')),
    path('Doctor/', include('Doctor.urls')),
    path('Receptionist/', include('Receptionist.urls')),
    path('admin/', admin.site.urls),
]