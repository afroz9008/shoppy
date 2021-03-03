from django.db import models

# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="uploades/categories/")

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_categories():
        return Categories.objects.all()


class Products(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=200, default="")
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to="uploades/products/")
    preparationTime = models.CharField(max_length=50, default=0)

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_products():
        return Products.objects.all()

    @staticmethod
    def get_all_products_by_id(categoryId):
        if categoryId:
            return Products.objects.filter(category=categoryId)
        else:
            return Products.objects.all()

    @staticmethod
    def get_product_by_id(productId):
        if productId:
            return Products.objects.filter(id=productId)
        else:
            return []


class SpecialItems(models.Model):
    active = models.BooleanField(default=False, name="Active_InActive_SpecialItem")
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, default="")
    image = models.ImageField(upload_to="uploades/SpecialItems/")
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, default=1)
    item = models.ForeignKey(Products, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_items():
        return SpecialItems.objects.all()