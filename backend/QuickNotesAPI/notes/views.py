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
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True) # pass the serializer the instance (object(s)) that you want it to serializer
    # Remember it will auto map the data since we define the innter meta class
    # If we are getting a container/wrapper that contains many objects, we have to set the 
    # argument value of many to True to let the serializer know that there are many objects

    return Response(serializer.data, status=status.HTTP_200_OK)
    # The Response function auto wraps any datatype in the correct pythonic container

  def post(self, request):
    serializer = NoteSerializer(data=request.data) # Deserialization of Incoming request data

    if serializer.is_valid(): # Validation of request
      serializer.save() # saving instance to database
      return Response(serializer.data, status=status.HTTP_201_CREATED) # returning newly created note in reponse 
  
    # Non valid request data
    return Response(status=status.HTTP_400_BAD_REQUEST)  


# Function Based View 
@api_view(['GET', 'PATCH', 'DELETE']) # Defining what HTTP methods it has access to
# In the REST Framework, the endpoint is responsible for a resource: in this case its the note
# It does not violate SRP if this singular endpoint is allowed to do multiple HTTP methods
def NoteDetailsView(request, note_id):

  # Querying for specific record and handleing does not exist error
  try:
    note = Note.objects.get(pk=note_id)
  except Note.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    serializer = NoteSerializer(note)
    return Response(serializer.data, status=status.HTTP_200_OK)

  if request.method == 'PATCH':
    serializer = NoteSerializer(note, data=request.data, partial=True)
    # To updated (PUT or PATCH a record) we have to pass the serializer the the specific
    # record first, and then the updating data (from the request)
    # The serializer looks at the updated fields from the request and compares it to the instance
    # In a PATCH request, the serializer has to also be set to partial=True so it knows that
    # we can pass partial (PATCH updated) (validation redundency)
    if serializer.is_valid(): # checking validation after data update
      serializer.save()

      return Response(serializer.data, status=status.HTTP_200_OK)
    
  
  if request.method == "DELETE":
    note.delete()
    return Response(status=status.HTTP_200_OK)

  return Response(status=status.HTTP_400_BAD_REQUEST)


# How Views and Serializers work together
  # 1) DRF view reads the request data
  # 2) Serializer validated input
  # 3) View checks .is_valid on serializer 
    # and calls .save() if serializer is valid
    # (VIEW ONLY WORKS WITH SERIALIZER AND NOTHING ELSE)
  # 4) DRF returns Response
    # Reponse(data(serializer data), status_code)
