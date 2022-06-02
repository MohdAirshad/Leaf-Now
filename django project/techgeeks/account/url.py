from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.account),
    path('login',views.login),
    path('signup',views.signup),
    path('dashboard/',views.dashboard),
]