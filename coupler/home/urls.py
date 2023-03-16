from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('signout',views.signout,name="signout"),
    path('social',views.social,name='social'),
    path('dashboard',views.dashboard, name='dashboard'),
    path('detail',views.detail, name='detail'),
    path('detaila',views.detaila, name='detaila'),
    path('preference1',views.preference1, name='preference1'),
    path('preference2',views.preference2, name='preference2'),
    path('blog',views.blog, name='blog'),
    path('blogpost',views.blogpost, name='blogpost'),
    path('blogcontact',views.blogcontact, name='blogcontact'),
    path('blogabout',views.blogabout, name='blogabout'),
    path('profile_list', views.profile_list, name='profile_list'),
    path('match_list', views.match_list, name='match_list'),
    ]