from django.contrib import admin
from django.urls import path
from frontApp import views

urlpatterns = [
    path('',views.index, name='index'),
    path('login/',views.log_in, name='log_in'),
    path('home/',views.home, name='home'),
    path('log_out/', views.log_out, name='log_out'),
    path('admin/', admin.site.urls),
]