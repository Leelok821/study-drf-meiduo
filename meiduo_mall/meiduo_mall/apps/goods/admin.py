from typing import Any
from django.contrib import admin
from django.http.request import HttpRequest
from . import models
from celery_tasks.html.tasks import generate_static_list_search_html
# Register your models here.

class GoodsCategoryAdmin(admin.ModelAdmin):
    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        super().save_model(request, obj, form, change)
        generate_static_list_search_html.delay()

    def delete_model(self, request: HttpRequest, obj: Any) -> None:
        super().delete_model(request, obj)
        generate_static_list_search_html.delay()

admin.site.register(models.Goods)
admin.site.register(models.Brand)
admin.site.register(models.GoodsCategory, GoodsCategoryAdmin)
admin.site.register(models.GoodsChannel)
admin.site.register(models.GoodsSpecification)
admin.site.register(models.SKU)
admin.site.register(models.SkuImage)
admin.site.register(models.SkuSpecification)
admin.site.register(models.SpecificationOption)