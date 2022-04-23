from django.urls import path
from .views import *

urlpatterns = [
    # path('', get_main_page, name="main_page"),
    path('register/', register, name="register"),
    path('login/', login_func, name="login"),
    path('logout/', logout_func, name="logout"),
    path('', index, name="chat"),
    path('<str:room_name>/', room, name="room"),



]