from rest_framework import serializers
from .models import Products, Categories,SpecialItems

class ProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields=['id','name','price','category','image','description']


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields=['id','name','image']


class CardSerializers(serializers.ModelSerializer):
    class Meta:
        model = SpecialItems
        fields=['id','Active_InActive_SpecialItem','name','description','image','category','item']
