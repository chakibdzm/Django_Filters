from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        depth=1
        fields=["id","name","tagline","description","price"]
