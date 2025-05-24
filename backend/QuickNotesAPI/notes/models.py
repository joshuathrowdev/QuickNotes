from django.db import models

# Create your models here.
class Note(models.Model):
  title = models.CharField(verbose_name="Title", null=False, blank=False)
  body = models.TextField(verbose_name="Body", null=False, blank=False)
  created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

  def __str__(self):
    return self.title