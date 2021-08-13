from django.db import models

# Create your models here.

class Order(models.Model):
    jpuser = models.ForeignKey('jpuser.Jpuser', on_delete=models.CASCADE, verbose_name='사용자') #on_delete를 써줘야한다. 사용자가 삭제될 때 어떻게 될지, cascade는 같이 삭제
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, verbose_name='상품')
    quantity = models.IntegerField(verbose_name='수량')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')
    
    def __str__(self):
        return str(self.jpuser) + ' ' + str(self.product)

    class Meta:
        db_table = 'xmart_order'
        verbose_name = '주문'
        verbose_name_plural = '주문'