from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from .forms import BookForm
from .models import Book
from django.apps import apps


def index(request):
    p = Paginator(Book.objects.all(), 3)
    page = request.GET.get('page')
    books = p.get_page(page)
    nums = "a" * books.paginator.num_pages

    return render(request, 'main/index.html', {'title': 'Главная',
                                               'books': books,
                                               'nums': nums,
                                               })


def create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    form = BookForm()
    context = {'form': form}
    return render(request, 'main/create_book.html', context)


# Delete a Venue
def delete_book(request, book_id):
    venue = Book.objects.get(pk=book_id)
    venue.delete()
    return redirect('home')


def update_book(request, book_id):
    venue = Book.objects.get(pk=book_id)
    form = BookForm(request.POST or None, request.FILES or None, instance=venue)
    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'main/update_book.html',
                  {'venue': venue,
                   'form': form
                   })
