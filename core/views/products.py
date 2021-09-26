from django.shortcuts import render
from django.views.generic import ListView

from core.models import ProductModel


class ProductListView(ListView):
    model = ProductModel
    template_name = 'main/products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['PAGE_TITLE'] = '商品一覧'

        return context

