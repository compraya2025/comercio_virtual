from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from applications.users.models import User


class AuditLog(models.Model):
    ACTION_CHOICES = (
        ('CREATE', 'Crear'),
        ('UPDATE', 'Actualizar'),
        ('DELETE', 'Eliminar'),
    )

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    
    # Relación genérica:
    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT)  # Qué modelo
    object_id = models.PositiveIntegerField()                                # ID del objeto
    content_object = GenericForeignKey('content_type', 'object_id')           # objeto real

    object_repr = models.TextField()     # Representación en texto (ej: str del objeto)
    changes = models.JSONField(null=True, blank=True)  # Cambios opcionales
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.timestamp} - {self.user} - {self.action} - {self.content_type} ({self.object_id})"