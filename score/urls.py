from django.urls import path
from . import views


app_name = 'score'

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='home'),
    path("alterar-pontuacao/", views.ModifyView.as_view(), name="alterar"),
    path("reset/", views.ResetView.as_view(), name="reset"),
    path("status/", views.StatusView.as_view(), name="status"),
]
