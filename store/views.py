from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status 
from .models import Product, Collection, Review
from .serializers import ProductSerializer, CollectionSerializer, ReivewSerializer
from django.db.models import Count
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['collection_id', ]

    def get_serializer_context(self):
        return {'request':self.request}   
 
class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.annotate(products_count=Count('products')).all()
    serializer_class =  CollectionSerializer
        
    def delete(self,request,pk):
        collection = get_object_or_404(
        Collection.objects.annotate(products_count=Count('products')), pk = pk)
        if collection.products.count() > 0:
            return Response({'messege':'Cannot delete '}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        collection.delete()
        return Response('Item deleted successfully .. ')

class ReviewViewSet(ModelViewSet):
    serializer_class = ReivewSerializer

    def get_queryset(self):
        return Review.objects.filter(product_id = self.kwargs['product_pk']).all()

    def get_serializer_context(self):
        return {"product_pk":self.kwargs['product_pk']}