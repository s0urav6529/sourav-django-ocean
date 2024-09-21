from django.urls import path

# if * files import in __init__ file then directly import from views
from .views import Home, Sign_in

urlpatterns = [
    path('', Home.as_view(), name='home_list'),
    path('add/', Home.as_view(), name='friend_add'),
    path('edit/<int:id>/', Home.as_view(), name='friend_edit'),
    path('delete/<int:id>/', Home.as_view(), name='friend_delete'),
]
