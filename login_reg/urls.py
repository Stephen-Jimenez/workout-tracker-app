from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user),
    path('logout', views.logout_user),
    path('create', views.register_user),
    path('edit_profile', views.edit_profile),
    path('password/', views.edit_password)
]