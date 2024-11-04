from django.urls import path
from . import views

urlpatterns = [
    path('client/<int:client_id>/orders/', views.client_orders, name='client_orders'),
]
