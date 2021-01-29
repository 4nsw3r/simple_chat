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
    fk_name = 'user'

###########################
class CustomUserAdmin(UserAdmin):
    inlines = (UserInline, )
    list_select_related = ('userprofile', )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
