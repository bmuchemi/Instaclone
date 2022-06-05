from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Image
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