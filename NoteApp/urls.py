from django.urls import path

from .views import getRoutes,getNote, getNoteDetail, createNote,updateNote,deleteNote

urlpatterns = [
    path('',getRoutes , name="getRoutes"),

    path('task_list/',getNote , name="notes"),

    path('task-create/',createNote , name="createNote"),

    path('task_list/<str:pk>/',getNoteDetail , name="getNoteDetail"),

    path('notes/<str:pk>/update/',updateNote , name="updateNote"),

    path('notes/<str:pk>/delete/', deleteNote, name="delete-note"),

]
