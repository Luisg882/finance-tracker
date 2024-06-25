from . import views
from django.urls import path

urlpatterns = [
    path('', views.ProfilePage.as_view(), name='home'),
]
