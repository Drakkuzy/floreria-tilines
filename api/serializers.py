from rest_framework.serializers import ModelSerializer
from core.models import Producto

class ProductoSerializer(ModelSerializer):
    class Meta:
        model = Producto
        exclude = ['stock']
        
