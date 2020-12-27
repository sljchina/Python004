from django.db import models

# Create your models here.

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=200)
    user_name = models.CharField(max_length=45)
    product_comment = models.CharField(max_length=300)
    score = models.CharField(max_length=45)

    # 定义显示格式
    def __str__(self):
        return "%d:%s:%s:%s:%s"%(self.id,self.product_name,self.user_name,self.product_comment,self.score)

    class Meta:
        db_table="mobile_commnets_score"
