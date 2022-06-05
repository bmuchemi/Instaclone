from django import forms
from .models import Image,Comment

class uploadForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile', 'likes', 'created_at']


class commentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['related_post', 'name' , 'created_at']