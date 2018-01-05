from django.db import models
import datetime

# Create your models here.

class UserInfo(models.Model):
    user = models.CharField(verbose_name='用户姓名',max_length=32)
    password = models.CharField(verbose_name='密码',max_length=64)

    class Meta:
        verbose_name = "用户表"

class Sign(models.Model):
    user = models.ForeignKey(verbose_name='用户',to='UserInfo')
    sign_date = models.DateTimeField(verbose_name='签到日期',auto_now_add=True)

    class Meta:
        verbose_name = "签到表"

    def save(self, *args, **kwargs):
        if self.sign_date:
            if self.sign_date.date() !=  datetime.date.today():
                raise ValueError("签到时间不匹配，必须为当前日期")
        super(Sign, self).save(*args, **kwargs)