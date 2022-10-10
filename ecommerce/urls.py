from django.urls import path
from ecommerce import views
urlpatterns = [
    #ecommerce
    path('products',views.ProductsView.as_view(),name='ecommerce-products'),
    path('productdetail',views.ProductDetailView.as_view(),name='ecommerce-productdetail'),
    path('orders',views.OrdersView.as_view(),name='ecommerce-orders'),
    path('customers',views.CustomersView.as_view(),name='ecommerce-customers'),
    path('cart',views.CartView.as_view(),name='ecommerce-cart'),
    path('checkout',views.CheckOutView.as_view(),name='ecommerce-checkout'),
    path('shops',views.ShopsView.as_view(),name='ecommerce-shops'),
    path('addproduct',views.AddProductView.as_view(),name='ecommerce-addproduct'),
]