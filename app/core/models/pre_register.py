from django.db import models

from app.utils.base_model import BaseModel


class PreRegister(BaseModel):
    email = models.EmailField(
        verbose_name='E-Mail',
        max_length=255,
        null=True, blank=True
    )
    category = models.ForeignKey(
        'core.Category',
        verbose_name='Category',
        on_delete=models.SET_NULL,
        related_name='pre_registers',
        null=True, blank=True
    )

    class Meta:
        verbose_name = 'Pre Register'
        verbose_name_plural = 'Pre Registers'
    
    def __str__(self):
        return self.email
    
