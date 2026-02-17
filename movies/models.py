from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    release_date = models.DateField(verbose_name="Дата выхода")

    def __str__(self):
        return self.title