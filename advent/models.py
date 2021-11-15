from django.db import models

class Date(models.Model):

    date = models.DateField()
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(blank=True, null=True)
    file = models.FileField(blank=True, null=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.date.strftime("%Y/%m/%d")