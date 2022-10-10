from django.urls import path
from crypto import views
urlpatterns = [
    #crypto
    path('wallet',views.WalletView.as_view(),name='crypto-wallet'),
    path('buysell',views.BuySellView.as_view(),name='crypto-buysell'),
    path('exchange',views.ExchangeView.as_view(),name='crypto-exchange'),
    path('lending',views.LendingView.as_view(),name='crypto-lending'),
    path('orders',views.OrdersView.as_view(),name='crypto-orders'),
    path('kycapllication',views.KYCView.as_view(),name='crypto-kycappication'),
    path('icolanding',views.ICOLandingView.as_view(),name='crypto-icolanding'),
]    