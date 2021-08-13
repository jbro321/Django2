from django.contrib import admin
from .models import Jpuser

# Register your models here.

class JpuserAdmin(admin.ModelAdmin):
    list_display = ('email', ) # 튜플로 인식하기 위해 , 꼭 써주기

admin.site.register(Jpuser, JpuserAdmin)