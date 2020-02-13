from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('delete/<str:stock_id>/', views.delete, name='delete'),
    path('delete_stock', views.delete_stock, name='delete_stock'),
]
