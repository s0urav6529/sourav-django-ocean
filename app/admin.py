from django.contrib import admin
from models import Friend

class AdminFriend(admin.ModelAdmin):
    list_display = ['id', 'nick_name', 'first_name', 'last_name']
    ordering = ('id',)

admin.site.register(Friend, AdminFriend)