from django.urls import path
from . import views
urlpatterns = [
 # path('login', views.login,name='login'),
 path('myview', views.myview,name='myview'),
 path('myview2', views.myview2,name='myview2'),
 # path('signup', views.signup,name='signup'),
 # path('logout',views.logout_user, name="logout"),

]