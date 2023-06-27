from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/<str:material>/', views.busqueda),
    path('search/', views.busqueda, name='search'),
    path('publish_offer/', views.publish_offer, name='publish_offer'),
    path('offer_detail/<int:pk_offer>/', views.offer_detail, name='offer_detail'),
    path('saled_offer/<int:pk_offer>/', views.saled_offer, name='saled_offer'),
    path('buy_offer/<int:pk_offer>/', views.buy_offer, name='buy_offer'),
    path('published_offers/<int:pk_usuario>/', views.published_offers, name='published_offers'),
    path('sales_history/', views.sales_history, name='sales_history'),
    path('shopping_history/', views.shopping_history, name='shopping_history'),
    path('delete_offer/<int:pk_offer>/', views.delete_offer, name='delete_offer'),
    path('articulo_comprado/', views.articulo_comprado, name='articulo_comprado'),
    path('mensajes/', views.mensajes, name='mensajes'),
    path('mensaje-visto/<int:pk_mensaje>/', views.mensaje_visto, name='mensaje_visto')
]
