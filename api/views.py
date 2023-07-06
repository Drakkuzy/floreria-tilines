from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductoSerializer
from rest_framework import status
from core.models import Producto
from .models import Suscripcion

@api_view(['GET'])
def productos(request):
    productos = Producto.objects.all()
    serializer = ProductoSerializer(productos, many=True)
    return Response(serializer.data, status.HTTP_200_OK)


@api_view(['GET'])
def suscrito(request, email):
    try:
        user = Suscripcion.objects.get(user=request.user)
        return Response({"Suscrito":user.suscrito}, status.HTTP_200_OK)
    except Suscripcion.DoesNotExist:
        return Response({"Mensaje":"Usuario no existe!."}, status.HTTP_204_NO_CONTENT)
    
