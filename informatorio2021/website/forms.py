from django import forms
from .models import Comment, Post

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('titulo','autor', 'cuerpo')

        widget = {
            'titulo': forms.TextInput(attrs={'class':'form-control'}),
            'autor': forms.Select(attrs={'class':'form-control'}),
            'cuerpo': forms.Textarea(attrs={'class':'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('titulo','autor', 'cuerpo')

        widget = {
            'titulo': forms.TextInput(attrs={'class':'form-control'}),
            'autor': forms.Select(attrs={'class':'form-control'}),
            'cuerpo': forms.Textarea(attrs={'class':'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('name','body')

        widget = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}), 
        }