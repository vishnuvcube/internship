from django.db import models

class GeneratedPassword(models.Model):
    generated_password = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

# Create your models here.
