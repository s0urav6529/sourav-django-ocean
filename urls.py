from django.urls import path

# if * files import in __init__ file then directly import from views
from views import Home, Sign_in

urlpatterns = [
    path('/', Home.as_view(), name = 'home'),
    path('sign_in/', Sign_in.as_view(), name = 'sign_in'),
]
