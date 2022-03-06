from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, View

from .forms import (
    AlbumAddForm,
    AlbumUpdateForm,
    BookAddForm,
    BookUpdateForm,
    MovieAddForm,
    MovieUpdateForm,
    TagAddForm,
    TagUpdateForm,
)

from .models import (
    Album,
    Book,
    Movie,
    Tag,
)

from view_classes import (
    BaseAddView,
    BaseUpdateView,
    BaseDeleteView,
)


class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        albums = Album.objects.order_by('-created_at')[:5]
        books = Book.objects.order_by('-created_at')[:5]
        movies = Movie.objects.order_by('-created_at')[:5]
        tags = Tag.objects.order_by('name')

        return render(
            request,
            'media/index.html',
            {
                'album_list': albums,
                'book_list': books,
                'movie_list': movies,
                'tag_list': tags,
            },
        )


class AlbumList(LoginRequiredMixin, ListView):
    model = Album


class AlbumAdd(BaseAddView):
    form_class = AlbumAddForm
    template_name = 'media/album_form.html'
    redirect_target = 'media:album_list'


class AlbumUpdate(BaseUpdateView):
    model_class = Album
    form_class = AlbumUpdateForm
    template_name = 'media/album_form.html'
    redirect_target = 'media:album_list'


class AlbumDelete(BaseDeleteView):
    model_class = Album
    redirect_target = 'media:album_list'


class BookList(LoginRequiredMixin, ListView):
    model = Book


class BookAdd(BaseAddView):
    form_class = BookAddForm
    template_name = 'media/book_form.html'
    redirect_target = 'media:book_list'


class BookUpdate(BaseUpdateView):
    model_class = Book
    form_class = BookUpdateForm
    template_name = 'media/book_form.html'
    redirect_target = 'media:book_list'


class BookDelete(BaseDeleteView):
    model_class = Book
    redirect_target = 'media:book_list'


class MovieList(LoginRequiredMixin, ListView):
    model = Movie


class MovieAdd(BaseAddView):
    form_class = MovieAddForm
    template_name = 'media/movie_form.html'
    redirect_target = 'media:movie_list'


class MovieUpdate(BaseUpdateView):
    model_class = Movie
    form_class = MovieUpdateForm
    template_name = 'media/movie_form.html'
    redirect_target = 'media:movie_list'


class MovieDelete(BaseDeleteView):
    model_class = Movie
    redirect_target = 'media:movie_list'


class TagList(LoginRequiredMixin, ListView):
    model = Tag


class TagAdd(BaseAddView):
    form_class = TagAddForm
    template_name = 'media/tag_form.html'
    redirect_target = 'media:tag_list'


class TagUpdate(BaseUpdateView):
    model_class = Tag
    form_class = TagUpdateForm
    template_name = 'media/tag_form.html'
    redirect_target = 'media:tag_list'


class TagDelete(BaseDeleteView):
    model_class = Tag
    redirect_target = 'media:tag_list'
