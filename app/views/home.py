from django.views import View
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.http import HttpResponse

from app.forms import FriendForm
from app.models import Friend

class Home(View):
    
    # for get request
    def get(self, request):
        form = FriendForm()
        friends = Friend.objects.all()
        context = {
            'form' : form,
            'friend' : friends
        }
        return render(request, 'home.html', context)
    
    # for post request
    def post(self, request):
        
        form = FriendForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('home')
        
        # if error
        friends = Friend.objects.all()
        context = {
            'form' : form,
            'friend' : friends
        }
        return render(request, 'home.html', context)
    
    def put(self, request, friend_id):
        
        #if not found instant 404 message
        friend = get_object_or_404(Friend, id=friend_id)
        
        form = FriendForm(request.PUT, instance=friend)
        
        if form.is_valid():
            form.save() 
            return HttpResponse('Friend updated successfully', status=200)
        return HttpResponse('Invalid data', status=400)
    
            
            