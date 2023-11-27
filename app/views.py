from django.shortcuts import render

from app.models import Post

# Create your views here.
def home(request):
    post = Post.objects.all()
    return render(request,"index.html",{'post':post})