from rest_framework import generics, serializers
from .models import Note

# Serializer converts Note model instances to JSON
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'content']

# GET (all notes) and POST (create note)
class NoteList(generics.ListCreateAPIView):
    queryset = Note.objects.all().order_by('-id')
    serializer_class = NoteSerializer

# GET (single), PUT (update), and DELETE
class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer