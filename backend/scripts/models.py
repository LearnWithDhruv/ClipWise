from django.db import models

class Script(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(default="Default content")  
    language = models.CharField(max_length=50, default='English')
    created_at = models.DateTimeField(auto_now_add=True)

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
