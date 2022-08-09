from django.shortcuts import render

from rest_framework.response import Response

from rest_framework.decorators import api_view

from django.http import JsonResponse

from .serializers import NoteSerializer
from .models import NoteModel


# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint' : '/task_list/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of task'
        }

    ]

    return Response(routes)




@api_view(["GET"])
def getNote(request):
    notes = NoteModel.objects.all().order_by('-created')
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

    pass



@api_view(["GET"])
def getNoteDetail(request, pk):
    notes = NoteModel.objects.get(id=pk)
    serializer = NoteSerializer(notes, many=False)
    return Response(serializer.data)

    pass


@api_view(["POST"])
def createNote(request):
    serializer = NoteSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

    pass



@api_view(["PUT"])
def updateNote(request, pk):
    note = NoteModel.objects.get(id = pk)
    serializer = NoteSerializer(instance= note,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

    pass


@api_view(['DELETE'])
def deleteNote(request, pk):
    note = NoteModel.objects.get(id=pk)
    note.delete()
    return Response('Note was deleted!')
