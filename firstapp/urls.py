from django.urls import path

from firstapp.views import *

urlpatterns = [
    path('', hellodjango),
    path('date', get_date),
    path('date/<str:unit>', get_date_info),
    path('<str:name>', hello_name),
]
