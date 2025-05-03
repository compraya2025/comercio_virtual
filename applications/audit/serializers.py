from rest_framework import serializers

from .models import Audit

class AuditSerializer(serializers.ModelSerializer):
    usuario_nombre = serializers.CharField(source="usuario.username", read_only=True)
    class Meta:
        model = Audit
        fields = ['producto','usuario_nombre', 'accion', 'created','modified']