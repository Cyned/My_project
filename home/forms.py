from django.contrib.auth.models import User
from django import forms
from .models import Post


class UserFormLog(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('caption', 'image', 'text')
