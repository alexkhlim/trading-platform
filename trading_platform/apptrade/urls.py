from API.views import (WatchListViewSet,
                       UserViewSet,
                       CurrencyViewSet,
                       InventoryViewSet,
                       OfferViewSet,
                       PriceViewSet,
                       TradeViewSet,
                       ItemViewSet,
                       CreateUserView,
                       )
from apptrade.views import RegisterFormView, LoginFormView
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r"user", UserViewSet)
router.register(r"currency", CurrencyViewSet)
router.register(r"item", ItemViewSet)
router.register(r"watch-list", WatchListViewSet)
router.register(r"price", PriceViewSet)
router.register(r"offer", OfferViewSet)
router.register(r"trade", TradeViewSet)
router.register(r"inventory", InventoryViewSet)

urlpatterns = [path('api/', include(router.urls)),
               path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
               path('register/', RegisterFormView.as_view()),
               path('register/token/', obtain_auth_token, name='token'),
               path('login/', LoginFormView.as_view()),
               path('users/register', CreateUserView.as_view()),
               ]
