from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='login'),
    path('profile',views.profile, name = 'profile'),
    path('post',views.post,name='posts'),
    path('createnewpost',views.create,name='create')
]