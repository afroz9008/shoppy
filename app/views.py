from django.shortcuts import render, HttpResponse
from app.models import Products, Categories,SpecialItems
from django.core import serializers
from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView 
from .serializers import ProductsSerializers,CategorySerializers,CardSerializers

# Get all Products Api
class ProductApiView(ListAPIView):
    queryset = Products.objects.all()
    serializer_class=ProductsSerializers
# Create Products Api
class ProductCreateApiView(CreateAPIView):
    queryset = Products.objects.all()
    serializer_class=ProductsSerializers
# Delete Products Api
class ProductDeleteApiView(DestroyAPIView):
    queryset = Products.objects.all()
    serializer_class=ProductsSerializers

# Get all Category Api.
class CategoryApiView(ListAPIView):
    queryset = Categories.objects.all()
    serializer_class=CategorySerializers
# Create Category Api
class CategoryCreateApiView(CreateAPIView):
    queryset = Categories.objects.all()
    serializer_class=CategorySerializers
# Delete Category Api
class CategoryDeleteApiView(DestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializers
    

# Card List Api
class CardApiView(ListAPIView):
    queryset = SpecialItems.objects.all()
    serializer_class=CardSerializers
# create Card Api.
class CardCreateApiView(CreateAPIView):
    queryset = SpecialItems.objects.all()
    serializer_class=CardSerializers
# Delete Card Api.
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


def ordersHistoryView(request):
    return render(request,"history.html")

def itemDetailView(request,id):
    print(request, id)
    product = Products.get_product_by_id(id)
    print(product)
    return render(request,"itemDetail.html",{ "product": product})