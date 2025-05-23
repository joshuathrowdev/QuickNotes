from django.contrib import admin

# Model imports
from .models import Note

# Register your models here.
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
  
  # Dynamic List Display (Method Override)
  def get_list_display(self, request):
    field_list = [field.name for field in self.model.meta.fields]
    return field_list