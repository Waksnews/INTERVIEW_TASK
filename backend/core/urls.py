from django.contrib import admin
from django.urls import path
from notes.views import NoteList, NoteDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Note endpoints: collection list/create and individual item lookup
    path('api/notes/', NoteList.as_view()),
    path('api/notes/<int:pk>/', NoteDetail.as_view()),
]