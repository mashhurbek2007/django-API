from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    path('', home, name="home"),
    path('krosovka-api/', krosovkaMakeApi),
    path('krosovka-api/<int:pk>/', singleAPI),
    path('create/', malumotJoylash),
    path('update/<int:pk>/', malumotupdate),
    path('delete/<int:pk>/', malumotDelete),
    path('search/', krosovkaSearch),
    path('filter/', filterKrosovka)
]
