from django.db import models

# Create your models here.
class Note(models.Model):
  title = models.CharField(verbose_name="Title", max_length=150, null=False, blank=False)
  body = models.TextField(verbose_name="Body", null=False, blank=False)

  def __str__(self):
    return self.title