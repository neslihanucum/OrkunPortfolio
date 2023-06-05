from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse


class Project(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    body = RichTextField(blank=True, null=True)
    project_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('orkun:home')