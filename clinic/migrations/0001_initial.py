# Generated by Django 3.2.4 on 2021-06-16 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200, verbose_name='问题')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
            options={
                'verbose_name': '问题',
                'verbose_name_plural': '问题',
            },
        ),
        migrations.CreateModel(
            name='Vip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vip_name', models.CharField(max_length=20, verbose_name='姓名')),
                ('vip_creat_date', models.DateTimeField(verbose_name='会员创建时间')),
                ('vip_guahao', models.IntegerField(default=9, verbose_name='挂号折扣')),
                ('vip_money', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='会员总金额')),
                ('vip_money_least', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='会员余额')),
                ('vip_xiaofei', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='本次消费')),
            ],
            options={
                'verbose_name': '会员',
                'verbose_name_plural': '会员',
            },
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.question')),
            ],
            options={
                'verbose_name': '选择',
                'verbose_name_plural': '选择',
            },
        ),
    ]