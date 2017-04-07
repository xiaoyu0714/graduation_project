from django.contrib import admin
from .models import User,Object,Order
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('borrow_date',)

admin.site.register(User)
admin.site.register(Object)
admin.site.register(Order,OrderAdmin)
