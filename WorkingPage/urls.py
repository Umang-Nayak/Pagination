from django.contrib import admin
from django.urls import path
from p1 import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('data/', views.User_Data),

]
