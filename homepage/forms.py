from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from homepage.models import Book, CustomUser

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['book']

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['book'].widget.attrs.update({
            'placeholder': 'Enter your books here',
            'cols' : '20',
            'rows' : '5',
        })

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'password1', 'password2','role')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password','role')
