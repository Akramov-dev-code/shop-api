from rest_framework import viewsets
from product.models import Product,  Category
from product .serializer import CategorySerializer



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer