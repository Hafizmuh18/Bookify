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

#CustomUserCreationForm instead of the default UserCreationForm, so we can add roles to user
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'password1', 'password2','role')

#Same as above, but only to modify
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password','role')
