from django.contrib import admin
from . models import Department, Role, Message,CustomUser,UserProfile

# Register your models here.
admin.site.register(Department)
admin.site.register(Role)
admin.site.register(Message)
admin.site.register(CustomUser)
admin.site.register(UserProfile)
