from django.shortcuts import render

from .forms import OrderForm

from telebot.sendmessage import send_telegram

from cms.services import get_slides
from price.services import get_price_cards, get_price_table
from .services import save_order


def first_page(request):
    slider_list = get_slides()
    pc = get_price_cards()
    price_table = get_price_table()
    form = OrderForm()
    context = {'slider_list': slider_list,
               'pc': pc,
               'price_table': price_table,
               'form': form,
               }
    return render(request, 'index.html', context)


def thanks_page(request):
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        save_order(name, phone)
        send_telegram(tg_name=name, tg_phone=phone)
        return render(request, 'thanks.html', {'name': name})
    else:
        return render(request, 'thanks.html')
