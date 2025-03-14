from django import forms

from . import models


class BookForm(forms.ModelForm):
    author = forms.CharField(max_length=10, widget=forms.TextInput, strip=True, required=True, label="author")
    title = forms.CharField(max_length=100, widget=forms.TextInput, strip=True, required=True, label="content")

    class Meta:
        model = models.Books
        fields = ['author', 'title']
