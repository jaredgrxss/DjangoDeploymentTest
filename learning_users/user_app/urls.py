from django.urls import path,include
from user_app import views

#INCLUDED TO ACCESS FROM OUR TEMPLATES
app_name = 'user_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register,name='register'),
    path('user_login/', views.user_login, name='user_login')
]