from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Message, UserProfile


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass



class UserInline(admin.StackedInline):
    model = UserProfile
    can_delete = False


class UserAdmin(UserAdmin):
    inlines = (UserInline, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
