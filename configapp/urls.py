from django.urls import path
from .views import *

urlpatterns = [
    path("index/",index,name='home'),
    path("salon/<int:pk>/",salonlar,name='salon'),
    path("brand/<int:salon>/<int:brand>/",brands,name='brand'),
    path("add_salon/",add_salons,name='add_salon'),
    path("add_brand/",add_brands,name='add_brand'),
    path("add_car/",add_cars,name='add_car')
]