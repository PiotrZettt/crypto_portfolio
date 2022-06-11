from django.urls import path
from . import views
from register import views as v
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('register/', v.register, name='register'),
    path('connect/', views.connect_to_binance, name='connect'),
    path('index/', views.index, name='index')
]
