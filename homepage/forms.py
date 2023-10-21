from django.forms import ModelForm
from homepage.models import Book

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