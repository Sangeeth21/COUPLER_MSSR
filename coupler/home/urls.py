from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('signout',views.signout,name="signout"),
    path('dashboard',views.dashboard, name='dashboard'),
    path('detail',views.detail, name='detail'),
    path('profile',views.profile, name='profile'),
    ] 