from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Goods)
admin.site.register(models.Brand)
admin.site.register(models.GoodsCategory)
admin.site.register(models.GoodsChannel)
admin.site.register(models.GoodsSpecification)
admin.site.register(models.SKU)
admin.site.register(models.SkuImage)
admin.site.register(models.SkuSpecification)
admin.site.register(models.SpecificationOption)

