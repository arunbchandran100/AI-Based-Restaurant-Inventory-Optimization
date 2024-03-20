from django.contrib import admin
from django.urls import path, include 
 

urlpatterns = [
    path('admin/', admin.site.urls),       
    path("", include("apps.authentication.urls")), # Auth routes - login / register

    # ADD NEW Routes HERE
    #path("some-route/", include("apps.some_app.urls")),

    # Leave `Home.Urls` as the last line
    path("", include("apps.home.urls"))
]
