from django.contrib import admin
from django.urls import include,path
from rest_framework import routers
from django.conf.urls import url
from .views import *
from . import views
from .views import pagelogout

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet)

urlpatterns = [
    path('', views.home , name="home"),
    path('api/', include(router.urls)),
    path('register' , register_attempt , name="register_attempt"),
    path('login' , login_attempt , name="login_attempt"),
    path('token' , token_send , name="token_send"),
    path('success' , success , name="success"),
    path('verify/<auth_token>' , verify , name="verify"),
    path('error' , error_page , name="error"),
    path('runcode', views.runcode),
    url('logout', pagelogout, name='logout'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/posts-delete/<str:pk>/', views.postDelete, name="posts-delete"),

]
