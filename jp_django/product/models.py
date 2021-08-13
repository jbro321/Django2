from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=256,verbose_name='상품명')
    price = models.IntegerField(verbose_name='상품가격')
    description = models.TextField(verbose_name='상품설명') #텍스트필드는 길이 제한이 없다.
    stuck = models.IntegerField(verbose_name='상품')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')
    
    def __str__(self): # 상품명으로 나타내기 위함
        return self.name

    class Meta:
        db_table = 'xmart_product'
        verbose_name = '상품'
        verbose_name_plural = '상품'