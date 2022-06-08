from django.urls import reverse
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect
from .models import Image,Profile,Comment
from django.contrib.auth.models import User
from .forms import uploadForm,commentForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/accounts/login/')
def feed(request):
    person = User.objects.filter(id=request.user.id)
    pictures = Image.objects.all()
    number = Comment.objects.count()
    return render(request, 'feed.html', {'pictures':pictures, 'number':number, 'person':person})

@login_required(login_url='/accounts/login/')
def profile(request,user_id):  
    users = User.objects.filter(id=user_id)     
    return render(request, 'profile.html', {'users':users})

def user(request, profile_id):
    users = Profile.objects.filter(id=profile_id)
    pics = Image.objects.filter(profile=profile_id).all()    
    return render(request, 'user.html', {'pics':pics, 'users':users}) 

@login_required(login_url='/accounts/login/')
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

@login_required(login_url='/accounts/login/')
def comments(request, id):
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


def like_post(request,pk):
    post = get_object_or_404(Image, id = request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('likes.html', args=[str(pk)]))  

   