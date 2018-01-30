from django.contrib import admin
from demo.models import UserMessage


class UserMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'address', 'message', )


# Register your models here.
admin.site.register(UserMessage, UserMessageAdmin)
