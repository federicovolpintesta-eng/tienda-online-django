from django.urls import path
from . import views, cart_views 
from . import order_views

app_name = 'tienda'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('cart/', cart_views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', cart_views.cart_add, name='cart_add'),
    path('cart/remove/<int:product_id>/', cart_views.cart_remove, name='cart_remove'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('order/create/', order_views.order_create, name='order_create'),
]