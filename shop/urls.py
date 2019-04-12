from django.urls import path
#from .views import item_list, item_detail, shop_list, shop_detail
from . import views

app_name = 'shop'

urlpatterns = [
    path('items/', views.item_list),
    path('items/<int:pk>/', views.item_detail),
    path('shop/', views.shop_list),
    path('shop/<int:pk>/', views.shop_detail),
]
