from rest_framework import serializers 
from .models import Product, Collection, Review
from decimal import Decimal

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title','products_count']
    products_count = serializers.IntegerField(read_only = True)




class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','title','unit_price','collection','price_with_tax']
    price_with_tax = serializers.SerializerMethodField(method_name='calc_tax')

    def calc_tax(self, product:Product):
        return product.unit_price * Decimal(1.1)


class ReivewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'name', 'description' ,'date']

    def create(self, validated_data):
        product_id = self.context['product_pk']
        return Review.objects.create(
            product_id = product_id,
            **validated_data
        )

