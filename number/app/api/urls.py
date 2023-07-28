from django.urls import path, include
from app.api import views
from .views import Numbers

urlpatterns = [
    path('numbers/', Numbers.as_view(), name='numbers'),
]
