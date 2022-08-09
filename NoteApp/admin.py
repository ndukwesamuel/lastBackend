from django.contrib import admin

# Register your models here.

from .models import NoteModel

admin.site.register(NoteModel)