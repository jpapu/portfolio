from django import forms
from .models import Comment, Post, Category

choices = Category.objects.all().values_list('name','name')

choice_list = []

for choice in choices:
    choice_list.append(choice)

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'title_tag', 'author', 'category', 'summary', 'body', 'header_image']

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'New Post Title'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Few word description'}),
            'author': forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'username', 'type':'hidden'}),
            'category': forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            'summary': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Short description'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        }

class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'title_tag', 'summary', 'body']

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'New Post Title'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Short Description'}),
            'summary': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Short description'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        }