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
            'cols': '20',
            'rows': '5',
        })

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'role')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'role')

class RegistrationForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    role = forms.ChoiceField(choices=CustomUser.ROLES, label='Role')
    address = forms.CharField(label='Address', required=False)
    phone_number = forms.CharField(label='Phone Number', required=False)
    date_of_birth = forms.DateField(label='Date of Birth', required=False)
