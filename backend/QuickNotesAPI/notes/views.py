# Giving API JSON Response
from rest_framework.response import Response
# HTTP Method (decorator)
from rest_framework.decorators import api_view # Only for function based views
# API Status codes
from rest_framework import status

from rest_framework.views import APIView # Only for testing API Directy (the rendering is handled by frontend)

# Model Imports
from .models import Note

# Serializer Import
from .serializers import NoteSerializer

# Create your views here.
# Class Based View (APIView)
class ListNotesView(APIView):
  # handle all HTTP Methods (by overriding APIView methods)
  # we override the HTTP methods that we want to
  # We have to pass the self pointer and the request

  def get(self, request):
    notes = Note.objects.get()
    serializer = NoteSerializer(notes) # pass the serializer the instance (object(s)) that you want it to serializer
    # Remember it will auto map the data since we define the innter meta class

    return Response(serializer.data, status=status.HTTP_200_OK)
  # The Response function auto wraps any datatype in the correct pythonic container


# Function Based View 
@api_view(['GET']) # Defining what HTTP methods it has access to
def NoteDetailsView(request, note_id):

  if request.method == 'GET':
    try:
      note = Note.objects.get(pk=note_id)
      serializer = NoteSerializer(note)

      return Response(serializer.data, status=status.HTTP_200_OK)
    except:
      return Response(status=status.HTTP_400_BAD_REQUEST)




# How Views and Serializers work together
  # 1) DRF view reads the request data
  # 2) Serializer validated input
  # 3) View checks .is_valid on serializer 
    # and calls .save() if serializer is valid
    # (VIEW ONLY WORKS WITH SERIALIZER AND NOTHING ELSE)
  # 4) DRF returns Response
    # Reponse(data(serializer data), status_code)
