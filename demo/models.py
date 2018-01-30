from django.db import models


# Create your models here.
class UserMessage(models.Model):
    object_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20, verbose_name='姓名')
    email = models.CharField(max_length=50, verbose_name='邮箱')
    address = models.CharField(max_length=200, verbose_name='家庭地址')
    message = models.CharField(max_length=200, verbose_name='留言信息')

    class Meta:
        verbose_name = '用户留言信息'
        db_table = 'UserMessage'
        ordering = ('-object_id',)

    def __unicode__(self):
        return self.name
