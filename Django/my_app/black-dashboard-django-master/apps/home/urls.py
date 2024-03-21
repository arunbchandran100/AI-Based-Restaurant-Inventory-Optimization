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

    #for viewing the details in the detabase
    path('/home/raw_materials.html', views.render_page, name='render_page'),
    path('fetch_food_items', views.fetch_food_items, name='fetch_food_items'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
