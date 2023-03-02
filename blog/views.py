from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    return render(request, 'blog/post_list.html', {})