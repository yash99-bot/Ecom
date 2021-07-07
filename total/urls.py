from django.urls import path
from . import views 
from django.conf.urls import include


  


urlpatterns = [
    path('1', index.as_view, name='index'),
    path('2/signup', Signup.as_view, name='signup'),
    path('3/login', Login.as_view, name='login'),
    path('4/logout', views.logout, name='logout'),
    path('5/cart', Cart.as_view, name='cart'),
    path('6/checkout', CheckOut.as_view, name='checkout'),
    path('7/orders', OrderView.as_view, name='orders'),
]