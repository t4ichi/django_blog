from django.shortcuts import render
from django.views.generic import TemplateView


class ProductListView(TemplateView):
    template_name = 'main/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['PAGE_TITLE'] = '商品一覧'

        return context
