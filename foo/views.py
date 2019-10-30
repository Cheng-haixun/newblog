# Create your views here.

from django.shortcuts import render,redirect
from .models import Blog

def Index(request):
    if (request.method ==
            "GET"):
        blogobj = Blog.objects.all()
        return render(
            request,
            'index.html',
            {'blogobj':blogobj}
            )