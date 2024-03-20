from django.urls import path, re_path
from apps.home import views
from .views import register
from .views import user_profile

urlpatterns = [

    path('register/', register, name='register'),
    # The home page
    path('', views.index, name='home'),
    
    path('user_profile/', user_profile, name='user_profile'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
