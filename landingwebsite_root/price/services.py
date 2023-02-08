from price.models import PriceCard, PriceTable


def get_price_table():
    price_table = PriceTable.objects.all()
    return price_table


def get_price_cards():
    price_cards = PriceCard.objects.all()
    return price_cards