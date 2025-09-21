from django import forms
from .models import Creator, Post

class CreatorForm(forms.ModelForm):
    class Meta:
        model = Creator
        fields = ['name', 'surname', 'age', 'image', 'bio', 'country']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'text', 'image', 'hashtags', 'video', 'country']
