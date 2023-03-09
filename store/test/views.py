from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
#ProductList is the one which contains both filter and search ..
class ProductList(ListAPIView):
     queryset=Product.objects.all()
     serializer_class=ProductSerializer
     filter_backends=(DjangoFilterBackend,SearchFilter)
     filterset_fields=['name']
     search_fields=['name']
    
class ProductDetail(APIView):
     def get(self,request,id):
          product= get_object_or_404(Product, pk=id)
          serializer=ProductSerializer(product)
          return Response(serializer.data)

     def put(self,request,id ):
          product= get_object_or_404(Product, pk=id)
          serializer=ProductSerializer(product,data=request.data)
          serializer.is_valid(raise_exception=True)
          serializer.save()
          return Response(serializer.data)
          

     def delete(self,request,id):
          product=get_object_or_404(Product,pk=id)
          if product.title.count()>0:
               return Response ({'error':'Product cannot be deleted'})
          Product.delete
          return Response(status=status.HTTP_204_NO_CONTENT)

