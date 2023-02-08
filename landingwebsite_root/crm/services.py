from .models import Order

def save_order(order_name, order_phone):
    element = Order(order_name=order_name, order_phone=order_phone)
    element.save()
