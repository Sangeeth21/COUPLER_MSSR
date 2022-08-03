from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('signout',views.signout,name="signout"),
    path('dashboard',views.dashboard, name='dashboard'),
    path('detail',views.detail, name='detail'),
    path('detaila',views.detaila, name='detaila'),
    path('profile',views.profile, name='profile'),
    path('preference1',views.preference1, name='preference1'),
    path('preference2',views.preference2, name='preference2'),


    ] 