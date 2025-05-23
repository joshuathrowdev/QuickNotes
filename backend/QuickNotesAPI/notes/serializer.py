# Serializers are responsible for
  # 3)  Serializing Python objects → JSON (response)
  # 2) Deserializing JSON → Python objects (request)
  # 3) Validating incoming data before saving

# They are the data layer between your models and your API.

# dependency import from the rest framework to define serializers
from rest_framework import serializers

# Model imports (since we are working with ModelSerializers)
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
  # Inner meta -> serves as the config center
  # Tells django how to map the serializer to the model correctly
  # What model are we mapping to, what fields are we mapping to (should we include all or exclude some)
  class Meta():
    model = Note # Corresponding Model for this serializer
    fields = [field.name for field in Note._meta.fields] # fields that we want to be serialized 



# Notes and workflow about Serializers
# 🔹 serializer.is_valid()
  # Runs validation on the data
  # Populates serializer.validated_data if valid
  # Use serializer.errors to inspect issues
# 🔹 serializer.save()
# Calls:
  # create() if instance=None (usually POST)
  # update() if instance=... (PUT/PATCH)