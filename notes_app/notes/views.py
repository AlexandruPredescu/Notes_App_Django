from django.shortcuts import render
from .models import Note
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


def homepage(request):

    return render(request, 'homepage.html',{
        'greetings': 'Welcome to our notes app'
    })


class NoteListView(ListView):
    model = Note
    template_name = 'notes_list.html'
    context_object_name = 'notes'


class NoteDetailView(DetailView):
    model = Note
    template_name = 'note_detail.html'


class NoteCreateView(CreateView):
    model = Note
    fields = ['title', 'text']
    template_name = 'note_form.html'
    success_url = '/notes'


class NoteUpdateView(UpdateView):
    model = Note
    fields = ['title', 'text']
    template_name = 'note_update.html'
    success_url = '/notes'


class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'confirm_delete_note.html'
    success_url = '/notes'



