# Generated by Django 3.2.4 on 2021-06-16 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vip',
            name='vip_guahao',
        ),
        migrations.RemoveField(
            model_name='vip',
            name='vip_money',
        ),
        migrations.RemoveField(
            model_name='vip',
            name='vip_money_least',
        ),
    ]
