from django.shortcuts import render
from django.views import generic
from .models import Post


class HomePageView(generic.ListView):
    model = Post
    template_name = 'posts/post_list.html'
