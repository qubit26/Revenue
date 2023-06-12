from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/<str:material>/', views.busqueda),
    path('search/', views.busqueda, name='search'),
    path('publish_offer/', views.publish_offer, name='publish_offer'),
    path('offer_detail/<int:pk_offer>/', views.offer_detail, name='offer_detail'),
    path('published_offers/', views.published_offers, name='published_offers'),
    path('sales_history/', views.sales_history, name='sales_history'),
    path('shopping_history/', views.shopping_history, name='shopping_history')
]
