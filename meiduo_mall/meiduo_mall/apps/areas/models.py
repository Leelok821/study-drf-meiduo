from django.db import models

# Create your models here.


# class Areas(models.Model):

#     name = models.CharField(verbose_name='名称', max_length=20)
#     parent = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='subs', null=True, blank=True, verbose_name='行政区划分')

#     class Meta:
#         db_table = 'tb_areas'
#         verbose_name = '行政区划'
#         verbose_name_plural = '行政区划'
    
#     def __str__(self) -> str:
#         return self.name




class Areas(models.Model):

    name = models.CharField(verbose_name='名称', max_length=20)
    parent = models.ForeignKey(verbose_name='行政区划分', to='self', on_delete=models.SET_NULL, related_name='subs', null=True, blank=True)

    class Meta:
        db_table = 'tb_areas'
    
    def __str__(self) -> str:
        return self.name