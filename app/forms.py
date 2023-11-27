from django import forms

from app.models import Post 

class AddForm(forms.ModelForm):
    class Meta:
        model = Post
        