from django.urls import path
from .views import classify_number

urlpatterns = [
    path('api/classify_number/', classify_number, name='number')
]