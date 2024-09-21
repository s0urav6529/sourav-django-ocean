from django.views import View
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from app.forms import FriendForm
from app.models import Friend

class Home(View):
    
    def get(self, request, id=None):
        
        if request.path == reverse('friend_list'): # instance list
            
            friends = Friend.objects.all().order_by('id')
            page = request.GET.get('page', 1)
            page_size = request.GET.get('page_size', 10)
            page_size = int(page_size) if str(page_size).isdigit() else 10

            paginator = Paginator(friends, page_size)

            try:
                friends = paginator.page(page)
                
            except (PageNotAnInteger, EmptyPage):
                friends = paginator.page(1)

            context = {
                'friends': friends,
                'page_size': page_size
            }
            return render(request,  + 'home_list.html', context)
            
        if id is None or id == 0: # create form

            form = FriendForm()
            context = {'url': 'friend_add', 'form': form}

        else:  # edit form
            
            friend = get_object_or_404(Friend, pk=id)
            form = FriendForm(instance=friend)
            context = {'url': 'friend_edit', 'form': form}
        
        return render(request, "friend_form.html", context)
    
    def post(self, request, id=None): # create & edit instance
        
        if '_method' in request.POST and request.POST['_method'] == 'DELETE':
            return self.delete(request, id) #call the delete method
        
        if id is None : #new instance
            form = FriendForm(request.POST)
            
        else:  #edit instance
            friend = get_object_or_404(Friend, pk=id)
            form = FriendForm(request.POST, instance=friend)
        
        if form.is_valid():
            form.save()
            
        return redirect('home_list')
    
    
    def delete(self, request, id=None): # delete an instance
        
        friend = get_object_or_404(Friend, pk=id)
        friend.delete()
        return redirect('home_list')
    
    
            
            