from django.db import models


class UzAuto(models.Model):
    nomi = models.CharField(max_length=255)
    rangi = models.CharField(max_length=255)
    narxi = models.CharField(max_length=255)

    def __str__(self):
        return self.nomi
