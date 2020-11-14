from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    path('read_csv/', views.read_csv, name='read_csv'),
]
