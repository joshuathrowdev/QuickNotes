from django.urls import path

# View (API Endpoit Logic) Imports 
from . import views as v

# Endpoint Paths go here
urlpatterns = [
  path('', v.ListNotesView.as_view(), name="notes_home_url"),
  path('<int:note_id>/', v.NoteDetailsView, name="note_details_url"),
]