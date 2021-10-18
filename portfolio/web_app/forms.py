from django import forms
from .models import Post, Category

choices = Category.objects.all().values_list('name','name')

choice_list = []

for choice in choices:
    choice_list.append(choice)

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'title_tag', 'author', 'category', 'body']

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'New Post Title'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Short Description'}),
            'author': forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'username', 'type':'hidden'}),
            #'author': forms.Select(attrs={'class':'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            #'category': forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=choice_list),
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