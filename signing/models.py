from django.db import models
from .models import SignedDocument

class SignedDocument(models.Model):
    document = models.FileField(upload_to='documents/')
    signature = models.BinaryField()
