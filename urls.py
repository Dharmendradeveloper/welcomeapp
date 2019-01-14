from django.contrib import admin
from django.urls import path
from welcomeapp import views
from django.conf.urls import url
urlpatterns=[
           path('admin/',admin.site.urls),
           url(r"^welcomeapp$", views.welcome,name="welcome")
] 
           
