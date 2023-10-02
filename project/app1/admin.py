from django.contrib import admin
from app1.models import registration,cont,base,prod

# Register your models here.

@admin.register(registration)
class registrationAdmin(admin.ModelAdmin):
    list_display=('name','phone','pincode','email','address',)

@admin.register(cont)
class contAdmin(admin.ModelAdmin):
    list_display=('name','email','phone','message',)

@admin.register(base)
class baseAdmin(admin.ModelAdmin):
    list_display=('email',)
    
@admin.register(prod)
class prodAdmin(admin.ModelAdmin):
    pass


