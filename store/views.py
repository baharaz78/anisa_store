from django.shortcuts import render
from django.views import View
from . import models


class ListProductView(View):
    def get(self, request):
        products = models.Product.objects.filter(is_available=True)
        context = {
            'objects': products
        }
        return render(request, 'store/product-list.html', context)

    def post(self, request):
        ...
#
# class UpperCaseWords(View):
#     def get(self, request):
#         words = models.
