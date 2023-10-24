from django.core.management.base import BaseCommand
from api.models import Client, Quote, QuoteDetails, Shopper, QuoteAssignment, Grocery


def create_clients():
    Client.objects.create(name="Cliente 1", lat=1, long=5, email="client@client.cl")
    Client.objects.create(name="Cliente 2", lat=2, long=2, email="client2@client.cl")
    Client.objects.create(name="Cliente 3", lat=3, long=3, email="client3@client.cl")


def create_shopper():
    Shopper.objects.create(name="Shopper 1", capacity=100, email="shopper@shopper.cl")


def create_groceries():
    Grocery.objects.create(name="Tienda 1", lat=1, long=1, api_url="1.cl")
    Grocery.objects.create(name="Tienda 2", lat=1, long=6, api_url="2.cl")


def create_quote():
    # Quote 1
    Quote.objects.create(
        client=Client.objects.get(id=1), total_capacity=15, status="in progress"
    )
    QuoteDetails.objects.create(
        quote=Quote.objects.get(id=1),
        grocery=Grocery.objects.get(id=1),
        product_id="a",
        quantity=10,
        total_size=10,
        keyword="huevo",
        price=1000,
    )
    QuoteDetails.objects.create(
        quote=Quote.objects.get(id=1),
        grocery=Grocery.objects.get(id=2),
        product_id="b",
        quantity=10,
        total_size=5,
        keyword="huevo",
        price=1000,
    )
    # Quote 2
    Quote.objects.create(
        client=Client.objects.get(id=2), total_capacity=80, status="in progress"
    )
    QuoteDetails.objects.create(
        quote=Quote.objects.get(id=2),
        grocery=Grocery.objects.get(id=1),
        product_id="c",
        quantity=10,
        total_size=70,
        keyword="huevo",
        price=1000,
    )
    QuoteDetails.objects.create(
        quote=Quote.objects.get(id=2),
        grocery=Grocery.objects.get(id=2),
        product_id="d",
        quantity=10,
        total_size=10,
        keyword="huevo",
        price=1000,
    )
    # quote 3
    Quote.objects.create(
        client=Client.objects.get(id=1), total_capacity=30, status="in progress"
    )
    QuoteDetails.objects.create(
        quote=Quote.objects.get(id=3),
        grocery=Grocery.objects.get(id=1),
        product_id="a",
        quantity=10,
        total_size=15,
        keyword="huevo",
        price=1000,
    )
    QuoteDetails.objects.create(
        quote=Quote.objects.get(id=3),
        grocery=Grocery.objects.get(id=2),
        product_id="b",
        quantity=10,
        total_size=15,
        keyword="huevo",
        price=1000,
    )
    # Quote 4
    Quote.objects.create(
        client=Client.objects.get(id=2), total_capacity=70, status="in progress"
    )
    QuoteDetails.objects.create(
        quote=Quote.objects.get(id=2),
        grocery=Grocery.objects.get(id=1),
        product_id="c",
        quantity=10,
        total_size=65,
        price=1000,
    )
    QuoteDetails.objects.create(
        quote=Quote.objects.get(id=2),
        grocery=Grocery.objects.get(id=2),
        product_id="d",
        quantity=10,
        total_size=5,
        price=1000,
    )

    # quote 5
    Quote.objects.create(
        client=Client.objects.get(id=3), total_capacity=5, status="in progress"
    )
    QuoteDetails.objects.create(
        quote=Quote.objects.get(id=5),
        grocery=Grocery.objects.get(id=2),
        product_id="a",
        quantity=10,
        total_size=5,
        keyword="huevo",
        price=1000,
    )


def assign_quotes():
    QuoteAssignment.objects.create(
        shopper=Shopper.objects.get(id=1), quote=Quote.objects.get(id=1)
    )
    QuoteAssignment.objects.create(
        shopper=Shopper.objects.get(id=1), quote=Quote.objects.get(id=2)
    )
    QuoteAssignment.objects.create(
        shopper=Shopper.objects.get(id=1), quote=Quote.objects.get(id=3)
    )
    QuoteAssignment.objects.create(
        shopper=Shopper.objects.get(id=1), quote=Quote.objects.get(id=4)
    )
    QuoteAssignment.objects.create(
        shopper=Shopper.objects.get(id=1), quote=Quote.objects.get(id=5)
    )


class Command(BaseCommand):
    def handle(self, *args, **options):
        create_clients()
        create_shopper()
        create_groceries()
        create_quote()
        assign_quotes()
