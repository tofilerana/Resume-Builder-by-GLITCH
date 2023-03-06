from django.contrib import admin
from .models import Form
# Register your models here.
class By_admin(admin.ModelAdmin):
 list_display=('id','first_name','last_name','created_date')
admin.site.register(Form,By_admin)