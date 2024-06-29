from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('Ss.urls')),  # Asegúrate de que 'Ss' esté en minúsculas y coincida con el nombre de tu aplicación
]
