from django.db import models

from django_advent.storage_backends import PrivateMediaStorage
from django_advent.storage_backends import PublicMediaStorage

class Date(models.Model):

    date = models.DateField()
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(
        storage=PublicMediaStorage(), 
        upload_to='files/', blank=True, null=True)
    file = models.FileField(blank=True, null=True)
    is_read = models.BooleanField(default=False)
    is_commentable = models.BooleanField(default=False)

    def __str__(self):
        return self.date.strftime("%Y/%m/%d")

class Comment(models.Model):

    date = models.ForeignKey(Date, on_delete=models.CASCADE)
    comment = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment