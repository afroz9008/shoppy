from django.shortcuts import render, HttpResponse
from app.models import Products, Categories,SpecialItems
from django.core import serializers

# Create your views here.
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
