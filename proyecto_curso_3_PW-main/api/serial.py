from rest_framework import serializers

from .models import Libro

class LibroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Libro
        fields = ['id','titulo','genero','autor','publicacion','precio_venta']