from django.db import models
from django.contrib import admin

class BInfo(models.Model):
    DEVID = models.CharField(max_length=150)
    COCOS_CONSOLE_ROOT = models.CharField(max_length=150)
    NDK_ROOT = models.CharField(max_length=150)
    ANDROID_SDK_ROOT = models.CharField(max_length=150)
    ANT_ROOT = models.CharField(max_length=150)

class BInfoAdmin(admin.ModelAdmin):
    list_display=('DEVID','COCOS_CONSOLE_ROOT','NDK_ROOT','ANDROID_SDK_ROOT','ANT_ROOT')

admin.site.register(BInfo,BInfoAdmin)
# Create your models here.
