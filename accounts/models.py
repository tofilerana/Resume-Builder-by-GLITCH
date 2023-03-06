from datetime import datetime
from django.db import models

# Create your models here.
class User(models.Model):
 email=models.EmailField()
 passwd=models.CharField(max_length=255)
 created_date= models.DateTimeField(default=datetime.now)
 class Meta:
  ordering = ('-id',)