from django.contrib import admin

# Register your models here.
from .models import Question, Choice, Vip

admin.site.register(Question)
admin.site.register(Choice)
class VipAdmin(admin.ModelAdmin):
    fields = ['vip_name', 'vip_money', 'vip_xiaofei','vip_guahao','vip_creat_date']
    list_display= ['vip_name', 'vip_money_least', 'vip_money','vip_guahao','vip_creat_date']
admin.site.register(Vip, VipAdmin)
