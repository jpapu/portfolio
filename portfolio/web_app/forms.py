from django import forms
from .models import Post

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'title_tag', 'author', 'body']

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'New Post Title'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Short Description'}),
            'author': forms.Select(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        }

class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'title_tag', 'body']

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'New Post Title'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Short Description'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        }