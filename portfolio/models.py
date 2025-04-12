# portfolio/models.py
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=50)
    image = models.ImageField(upload_to='project_images/') # Stores images in MEDIA_ROOT/project_images/
    link = models.URLField(blank=True, null=True) # Optional link

    def __str__(self):
        return self.title