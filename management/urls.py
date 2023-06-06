from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.busqueda, name='search'),
    path('publish_offer/', views.publish_offer, name='publish_offer'),
    path('offer_detail/', views.offer_detail, name='offer_detail')
]
