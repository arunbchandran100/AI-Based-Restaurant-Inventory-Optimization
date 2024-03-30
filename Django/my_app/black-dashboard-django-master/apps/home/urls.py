from django.urls import path, re_path
from apps.home import views
from .views import register
from .views import user_profile
from .views import create_food_item
from django.urls import path
from .views import upload_dataset


urlpatterns = [

    path('register/', register, name='register'),
    # The home page
    path('', views.index, name='home'),
    
    path('/home/user_profile/', user_profile, name='user_profile'),
    path('create_food_item/', create_food_item, name='create_food_item'),

    #for viewing the details in the database
    path('/home/raw_materials.html', views.render_page, name='render_page'),
    path('fetch_food_items', views.fetch_food_items, name='fetch_food_items'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),
    
    path('upload/', upload_dataset, name='upload_dataset'),

]
