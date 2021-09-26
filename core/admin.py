from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import ProductModel, CategoryModel, TagModel, MakerModel


class ProductModelResource(resources.ModelResource):

    class Meta:
        model = ProductModel
        fields = ('id', 'name', 'maker', 'description', 'price',
                  'stock', 'is_published', 'model_year',
                  'category', 'tags')


@admin.register(ProductModel)
class ProductModelAdmin(ImportExportModelAdmin):
    resource_class = ProductModelResource


# Register your models here.
# admin.site.register(ProductModel)
admin.site.register(CategoryModel)
admin.site.register(TagModel)
admin.site.register(MakerModel)
