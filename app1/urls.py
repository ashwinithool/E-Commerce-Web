
from django.urls import path
from . import views
from .views import Index
from .views import CheckOut

urlpatterns = [
    path('',Index.as_view(), name="index"),
    path('signup', views.signup, name="signup"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('cart', views.cart, name="cart"),
    path('check-out', CheckOut.as_view(), name="checkout")
   
   
]