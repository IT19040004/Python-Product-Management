from django.urls import path

from . import views

urlpatterns = [

    path('', views.ShowAllProducts, name='showProducts'),

    path('product/<int:pk>', views.productDetail, name='product'),

    path('addProduct/', views.addProduct, name='addProduct'),

]