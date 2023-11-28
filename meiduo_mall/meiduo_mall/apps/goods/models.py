from django.db import models

# Create your models here.


class Brand(models):
    """
    品牌表
    """
    name = models.CharField(max_length=50, verbose_name='名称')
    logo = models.CharField(max_length=200, verbose_name='logo图片链接')
    first_letter = models.CharField(max_length=1, verbose_name='首字母')

class GoodsCategory(models):
    """
    商品类别表
    """
    name = models.CharField(max_length=10, verbose_name='名称')
    parent = models.ForeignKey(to='self', on_delete=models.PROTECT, )


class Goods(models):
    """商品表"""
    name = models.CharField(max_length=50, verbose_name='名称')
    brand = models.ForeignKey(to=Brand, on_delete=models.PROTECT, verbose_name='品牌id')
    category1 = models.ForeignKey()