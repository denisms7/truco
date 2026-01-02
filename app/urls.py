from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('admin/truco/', admin.site.urls),
    path('', include('score.urls')),
]
