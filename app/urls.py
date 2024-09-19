from django.urls import path

# if * files import in __init__ file then directly import from views
from .views import Home, Sign_in

urlpatterns = [
    # GET and POST requests for the Home view
    path('friend/', Home.as_view(), name='home'),

    # PUT request for updating a friend (uses <friend_id>)
    path('friend/<int:friend_id>/', Home.as_view(), name='friend_edit'),

    # DELETE request for deleting a friend (uses <friend_id>)
    path('friend/delete/<int:friend_id>/', Home.as_view(), name='friend_delete'),
]
