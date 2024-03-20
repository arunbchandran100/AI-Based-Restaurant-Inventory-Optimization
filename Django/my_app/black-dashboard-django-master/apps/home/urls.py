from django.urls import path, re_path
from apps.home import views
from .views import register

urlpatterns = [

    path('register/', register, name='register'),
    # The home page
    path('', views.index, name='home'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
