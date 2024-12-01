from django.shortcuts import render
from .models import Libro
from rest_framework import viewsets
from rest_framework.response import Response
from .serial import LibroSerializer

class LibroViewSet(viewsets.ModelViewSet):
    """
    API-REST endpoint para el modelo libro, admite
    GET, POST, PUT, PATCH, DELETE
    """
    queryset = Libro.objects.all().order_by('-publicacion')
    serializer_class = LibroSerializer
