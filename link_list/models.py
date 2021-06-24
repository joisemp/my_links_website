from django.db import models

class Link(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    image = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return str(self.name)