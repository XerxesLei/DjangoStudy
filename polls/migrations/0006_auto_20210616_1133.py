# Generated by Django 3.2.4 on 2021-06-16 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20210616_0936'),
    ]

    operations = [
        migrations.AddField(
            model_name='vip',
            name='vip_xiaofei',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='本次消费'),
        ),
        migrations.AlterField(
            model_name='vip',
            name='vip_money',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='会员总金额'),
        ),
        migrations.AlterField(
            model_name='vip',
            name='vip_money_least',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='会员余额'),
        ),
    ]