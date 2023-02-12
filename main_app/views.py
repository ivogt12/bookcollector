from django.shortcuts import render, redirect

from .models import Book, Review, Award

from .forms import ReviewForm

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# def books_index(request):
#     books = Book.objects.all()
#     return render(request, 'books/index.html', {
#         'books': books
#     })

class BookList(ListView):
    model = Book
    template_name = 'books/index.html'

def books_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    id_list = book.awards.all().values_list('id')
    awards_book_doesnt_have = Award.objects.exclude(id__in=id_list)
    review_form = ReviewForm()
    return render(request, 'books/detail.html', {
        'book': book, 'review_form': review_form,
        'awards': awards_book_doesnt_have
    })

def add_review(request, book_id):
    form = ReviewForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.book_id = book_id
        new_review.save()
    return redirect('detail', book_id=book_id)


class BookCreate(CreateView):
    model = Book
    fields = ['name', 'author', 'year_published', 'description']

class BookUpdate(UpdateView):
    model = Book
    fields = ['author', 'author', 'year_published', 'description']

class BookDelete(DeleteView):
    model = Book
    success_url = '/books'

class AwardList(ListView):
    model = Award

class AwardDetail(DetailView):
    model = Award

class AwardCreate(CreateView):
    model = Award
    fields = '__all__'

class AwardUpdate(UpdateView):
    model = Award
    fields = '__all__'

class AwardDelete(DeleteView):
    mdoel = Award
    fields = '__all__'

def assoc_award(request, book_id, award_id):
    Book.objects.get(id=book_id).awards.add(award_id)
    return redirect('detail', book_id=book_id)

def disassoc_award(request, book_id, award_id):
    Book.objects.get(id=book_id). awards.remove(award_id)
    return redirect('detail', book_id=book_id)