import datetime
from django.db import models

from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField('问题',max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self) -> str:
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    class Meta:
        verbose_name = '问题'
        verbose_name_plural = '问题'

class Choice(models.Model) :
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self) -> str:
        return self.choice_text

    class Meta:
        verbose_name = '选择'
        verbose_name_plural = '选择'

class Vip(models.Model) :
    vip_name = models.CharField('姓名', max_length=20)
    vip_creat_date = models.DateTimeField('会员创建时间')
    vip_guahao = models.IntegerField('挂号折扣',default=9)
    vip_money = models.DecimalField('会员总金额', max_digits=10, decimal_places=2, default=0)
    vip_money_least = models.DecimalField('会员余额', max_digits=10,decimal_places=2, default=0)
    vip_xiaofei = models.DecimalField('本次消费', max_digits=10, decimal_places=2, default=0)

    class Meta:
        verbose_name = '会员'
        verbose_name_plural = '会员'

    def __str__(self) -> str:
        return self.vip_name

    def save(self, *args, **kwargs):
        self.vip_money_least = self.vip_money + self.vip_money_least - self.vip_xiaofei
        return super().save(*args, **kwargs)