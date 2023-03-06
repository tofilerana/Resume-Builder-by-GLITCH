from django.contrib import admin
from .models import User
# Register your models here.
class By_admin(admin.ModelAdmin):
 list_display=('id','email','created_date')

admin.site.register(User,By_admin)