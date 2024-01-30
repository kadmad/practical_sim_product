from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, views
from product.models import Product, Category
from product.serializers import CategorySerializer, ProductSerializer
from rest_framework.permissions import IsAuthenticated
from django.views.generic import CreateView, ListView, View
from django.urls import reverse_lazy
from product.forms import ProductInputForm
from product.renderers import CustomRenderer


# Create your views here.
# API View Functions.
class CategoryAPI(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    renderer_classes = [CustomRenderer]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductAPI(viewsets.ModelViewSet):
    renderer_classes = [
        CustomRenderer,
    ]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# Django View Function
class PopulateProduct(CreateView):
    model = Product
    form_class = ProductInputForm
    template_name = "product/product_page.html"
    success_url = reverse_lazy("products")

    def form_valid(self, form) -> HttpResponse:
        form.save()
        return HttpResponseRedirect("/products")

    def form_invalid(self, form) -> HttpResponse:
        print("----------Error----------------", form.errors)
        return super().form_invalid(form)


class ProductList(ListView):
    model = Product
    template_name = "product/product_page.html"


class ProductListInfo(View):
    def get(self, request):
        result_list = list(
            Product.objects.all().values(
                "title",
                "description",
                "status",
                "price",
            )
        )
        return JsonResponse(result_list, safe=False)
