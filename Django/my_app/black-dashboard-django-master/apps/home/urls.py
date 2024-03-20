from django.urls import path, re_path
from apps.home import views
from .views import register
from .views import user_profile
from .views import create_food_item

urlpatterns = [

    path('register/', register, name='register'),
    # The home page
    path('', views.index, name='home'),
    
    path('user_profile/', user_profile, name='user_profile'),
    path('create_food_item/', create_food_item, name='create_food_item'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
