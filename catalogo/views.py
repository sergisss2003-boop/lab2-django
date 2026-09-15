from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Producto
from .serializers import ProductoSerializer

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'catalogo/lista.html', {'productos': productos})

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'catalogo/detalle.html', {'producto': producto})

class ProductoViewSet(viewsets.ViewSet):

    def list(self, request):
        productos = Producto.objects.all()
        return Response(ProductoSerializer(productos, many=True).data)

    def retrieve(self, request, pk=None):
        producto = Producto.objects.filter(id=pk).first()
        if not producto:
            return Response({'error': 'No encontrado'}, status=status.HTTP_404_NOT_FOUND)
        return Response(ProductoSerializer(producto).data)

    def create(self, request):
        serializer = ProductoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        producto = Producto.objects.create(**serializer.validated_data)
        return Response(ProductoSerializer(producto).data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        producto = Producto.objects.filter(id=pk).first()
        if not producto:
            return Response({'error': 'No encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        Producto.objects.filter(id=pk).update(**serializer.validated_data)
        return Response(ProductoSerializer(Producto.objects.get(id=pk)).data)

    def destroy(self, request, pk=None):
        producto = Producto.objects.filter(id=pk).first()
        if not producto:
            return Response({'error': 'No encontrado'}, status=status.HTTP_404_NOT_FOUND)
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)