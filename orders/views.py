from django.shortcuts import render
from .models import Client, Order
from datetime import timedelta
from django.utils import timezone

def client_orders(request, client_id):
    client = Client.objects.get(id=client_id)
    now = timezone.now()

    # За последние 7 дней
    orders_week = Order.objects.filter(client=client, created_at__gte=now - timedelta(days=7))

    # За последние 30 дней
    orders_month = Order.objects.filter(client=client, created_at__gte=now - timedelta(days=30))

    # За последние 365 дней
    orders_year = Order.objects.filter(client=client, created_at__gte=now - timedelta(days=365))

    # Получаем уникальные товары за каждый период
    products_week = set(product for order in orders_week for product in order.products.all())
    products_month = set(product for order in orders_month for product in order.products.all())
    products_year = set(product for order in orders_year for product in order.products.all())

    return render(request, 'orders/client_orders.html', {
        'client': client,
        'products_week': products_week,
        'products_month': products_month,
        'products_year': products_year,
    })
