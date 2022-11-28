from .models import Book
from django.forms import ModelForm, TextInput, Textarea


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["author", "name", "price", "description"]
        widgets = {"author": TextInput(attrs={'class': 'form-control',
                                              'type': 'text',
                                              'placeholder': 'Автор'
                                              }),
                   "name": TextInput(attrs={'class': 'form-control',
                                            'type': 'text',
                                            'placeholder': 'Название'
                                            }),
                   "description": Textarea(attrs={'class': 'form-control',
                                                  'type': 'text',
                                                  'placeholder': 'Описание'
                                                  }),
                   "price": TextInput(attrs={'class': 'form-control',
                                            'type': 'number',
                                            'placeholder': 'Цена',
                                            }),
                   }
