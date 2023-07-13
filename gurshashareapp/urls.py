from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("campaign/", views.campaign, name="campaign"),
    path("register/", views.register, name="register"),
    path("payment/<slug:slug>", views.payment, name="payment"),
    path("logout/", views.signout, name="logout"),
    
]
