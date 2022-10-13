from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class ImageUpload(models.Model):
    name = models.CharField(max_length=40)
    username = models.CharField(max_length=40)
    email = models.EmailField()
    picture = models.ImageField(upload_to="images/")
    date_uploaded = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
