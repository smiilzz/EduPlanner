from django.db import models
from django.core.exceptions import ValidationError

class Api(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    FechaInicio = models.DateField()
    FechaTermino = models.DateField()

    '''def clean(self):
        if self.FechaTermino and self.FechaInicio and self.FechaTermino < self.FechaInicio:
            raise ValidationError("La fecha de término no puede ser anterior a la fecha de inicio.")'''

    def __str__(self):
        return self.title