from django.db import models


class Contacts(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.name