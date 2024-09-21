from models import Friend
from django import forms


class FriendForm(forms.ModelForm):
    model = Friend
    fields = '__all__'