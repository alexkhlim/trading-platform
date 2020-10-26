from API.serializers import (
    TradeSerializer,
    WatchListSerializer,
    PriceSerializer,
    ItemSerializer,
    OfferSerializer,
    InventorySerializer,
    UserSerializer,
    CurrencySerializer,
)
from apptrade.models import Trade, Offer, Currency, Inventory, Item, WatchList, Price
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CurrencyViewSet(ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class WatchListViewSet(ModelViewSet):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer


class PriceViewSet(ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


class OfferViewSet(ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer


class TradeViewSet(ModelViewSet):
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer


class InventoryViewSet(ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
