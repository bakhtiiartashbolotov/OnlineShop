from . import views
from django.urls import path


urlpatterns = [
    path('', views.homepage, name='home'),
    path('tech', views.techpage, name='tech_page'),
    path('fashion', views.fashionpage, name='fashion_page'),
    path('auto', views.autopage, name='auto_page'),
    path('jewelery', views.jewelrypage, name='jewelry_page'),
    path('food', views.foodpage, name='food_page')
]