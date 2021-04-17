from django.shortcuts import render
from .models import User, Page, Post, Song
# Create your views here.

def home(request):
    return render(request, 'socialSite/home.html')


def user_func(request):
    all_users = User.objects.all()
    data_user_post = User.objects.filter(song__duration__gt='4')
    data_user_page = User.objects.filter(page__page_creations__gt='2021-2-17')
    return render(request, 'socialSite/user.html', {'all_users':all_users,'data_user_post':data_user_post, 'data_user_page':data_user_page})

def song_func(request):

    return render