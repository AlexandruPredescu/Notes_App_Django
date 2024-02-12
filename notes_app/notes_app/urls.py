"""
URL configuration for notes_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from notes.views import homepage, NoteListView, NoteDetailView, NoteCreateView, NoteUpdateView, NoteDeleteView


admin.site.site_header = 'Notes App'
admin.site.index_title = 'Notes App administration'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('notes/', NoteListView.as_view(), name='notes.list'),
    path('notes/<int:pk>/', NoteDetailView.as_view(), name='detail'),
    path('notes/new', NoteCreateView.as_view(), name='note.new'),
    path('notes/edit/<int:pk>/', NoteUpdateView.as_view(), name='note.update'),
    path('notes/delete/<int:pk>/', NoteDeleteView.as_view(), name='note.delete'),
]
