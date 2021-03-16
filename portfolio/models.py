from django.db import models


class Info(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField()

    class Meta:
        verbose_name = 'Info'
        verbose_name_plural = 'Info'

    def __str__(self):
        return f'{self.name}'
