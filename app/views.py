from django.shortcuts import render, HttpResponse
from app.models import Products, Categories,SpecialItems
from django.core import serializers
from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView 
from .serializers import ProductsSerializers,CategorySerializers,CardSerializers

# Create your views here.
class ProductApiView(ListAPIView):
    queryset = Products.objects.all()
    serializer_class=ProductsSerializers
# Create your views here.
class ProductCreateApiView(CreateAPIView):
    queryset = Products.objects.all()
    serializer_class=ProductsSerializers
# Create your views here.
class ProductDeleteApiView(DestroyAPIView):
    queryset = Products.objects.all()
    serializer_class=ProductsSerializers

# Create your views here.
class CategoryApiView(ListAPIView):
    queryset = Categories.objects.all()
    serializer_class=CategorySerializers
# Create your views here.
class CategoryCreateApiView(CreateAPIView):
    queryset = Categories.objects.all()
    serializer_class=CategorySerializers
# Create your views here.
class CategoryDeleteApiView(DestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializers
    

# Create your views here.
class CardApiView(ListAPIView):
    queryset = SpecialItems.objects.all()
    serializer_class=CardSerializers
# Create your views here.
class CardCreateApiView(CreateAPIView):
    queryset = SpecialItems.objects.all()
    serializer_class=CardSerializers
# Create your views here.
class CardDeleteApiView(DestroyAPIView):
    queryset = SpecialItems.objects.all()
    serializer_class=CardSerializers


def productView(request):
    product = None
    categories = Categories.get_all_categories()
    categoryId = request.GET.get("category")
    if categoryId:
        categoryId = int(categoryId)
        product = Products.get_all_products_by_id(categoryId)
    else:
        categoryId = int(categories[0].id)
        product = Products.get_all_products_by_id(categoryId)
    
    dataJSON = serializers.serialize('json', product)

    specialItems = SpecialItems.get_all_items()
    cardJSONData = serializers.serialize('json', specialItems)
    
    return render(
        request,
        "products.html",
        {
            "products": product,
            "jsonProducts":dataJSON,
            "categories": categories,
            "selectedCategoryId": categoryId,
            "specialCardItems": cardJSONData,
        },
    )
