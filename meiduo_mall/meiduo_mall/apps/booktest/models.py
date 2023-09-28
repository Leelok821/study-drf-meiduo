from django.db import models

# Create your models here.


class BookInfo(models.Model):
    btitle = models.CharField(verbose_name='名称',max_length=20)
    bpub_date = models.DateField(verbose_name='发布日期')
    bread = models.IntegerField(verbose_name='阅读量',default=0)
    bcomment = models.IntegerField(verbose_name='评论量', default=0)
    is_delete = models.BooleanField(verbose_name='逻辑删除', default=False)

    def __str__(self) -> str:
        return self.btitle


class HeroInfo(models.Model):
    GENDER_CHOICES = ((0, 'male'), (1, 'female'))
    hname = models.CharField(max_length=20, verbose_name='名称')
    hgender = models.SmallIntegerField(verbose_name='性别', choices=GENDER_CHOICES, default=0)
    hcomment = models.CharField(max_length=200, null=True, verbose_name='描述信息')
    hbook = models.ForeignKey(to=BookInfo, on_delete=models.CASCADE, verbose_name='所属书籍')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')