from django import forms 
from .models import Comment
from django.forms import Textarea, TextInput


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','email','subject', 'body')
        widgets = {
            'name': TextInput(attrs={'class':'form-control'}),
            'email': TextInput(attrs={ 'class':'form-control'}),
            'subject': TextInput(attrs={ 'class':'form-control'}),
            'body': Textarea(attrs={ 'class':'form-control'}),
        }


        
