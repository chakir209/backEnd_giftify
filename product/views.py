from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from product.serializers import ProductSerializer

@api_view(['GET', 'POST'])
def liste_products(request):
    if request.method == 'GET':
        cadeaux = Product.objects.all()
        serializer = ProductSerializer(cadeaux, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def detail_products(request, pk):
    cadeau = get_object_or_404(Product, pk=pk)

    if request.method == 'GET':
        serializer = ProductSerializer(cadeau)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductSerializer(cadeau, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cadeau.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
