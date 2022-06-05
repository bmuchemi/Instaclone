from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Image,Comment
from django.contrib.auth.models import User
from .forms import uploadForm

# Create your views here.

def feed(request):
    pictures = Image.objects.all()
    return render(request, 'feed.html', {'pictures': pictures})

def profile(request):
    current_user = request.user.profile
    pics = Image.objects.filter(profile=current_user).all()
    return render(request, 'profile.html', {'pics':pics})

def user(request, user_id):
    users = User.objects.filter(id=user_id)
    pics = Image.objects.filter(profile=user_id).all()    
    return render(request, 'user.html', {'pics':pics, 'users':users}) 


def new_image(request):
    current_user = request.user.profile
    if request.method == 'POST':
        form = uploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.profile = current_user
            image.save()
        return redirect('feed')
    else:
        form = uploadForm()
    return render(request, 'new_image.html', {'form':form})

def comments(request, image_id):
    current_user = request.user.profile
    post = Image.objects.filter(id=id)

    if request.method == 'POST':  
        form = commentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.name = current_user
            comment.related_post = post
            comment.save()
        return redirect('comments')

    else:
        form = commentForm()

        maoni = Comment.objects.filter(related_post=id).all()

    return render(request, 'comments.html', {'form':form, 'maoni':maoni})


def like_post(request, post_id):
    current_user = request.user
    img = Image.objects.get(id=post_id)
    if img.likes.filter(id=current_user.id).exists():
        img.likes.remove(current_user)
    else:
        img.likes.add(current_user)
    return redirect('feed')