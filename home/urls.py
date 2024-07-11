from django.contrib import admin  
from django.urls import path
from home import views
from django.urls import reverse

urlpatterns = [
    path("", views.index, name='home'),
  
    path('searchbar',views.searchbar, name='search'),
    path('book_desc/<int:pk>/',views.book_desc, name="book_desc"),
    path('yourbook',views.yourbook, name='book'),
    path('user_login',views.user_login, name='user_login'),
    path('user_register',views.user_register, name='user_register'),
    path('user_logout',views.user_logout, name='user_logout'),

    path('add_to_cart/<pk>',views.add_to_cart,name='add_to_cart'),
    path('cart',views.cart,name="cart"),

  


]


