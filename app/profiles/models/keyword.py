from django.db import models

class Keyword(models.Model):
    name = models.CharField(max_length = 150, unique=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Keyword'
        verbose_name_plural = 'Keywords'