from .models import Comment,Error
from django import forms

class ErrorForm(forms.ModelForm):
    class Meta:
        model = Error
        exclude=[]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude=[]
