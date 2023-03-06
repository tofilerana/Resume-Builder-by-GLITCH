from django.db import models
from datetime import datetime

# Create your models here.
class Form(models.Model):
 template_choice=(
  ('template1' ,"template1"),
  ('template2' ,"template2"),
 )
 userId=models.IntegerField()
 first_name=models.CharField(max_length=255)
 last_name=models.CharField(max_length=255)
 objective=models.CharField(max_length=255)
 projects=models.TextField()
 skills=models.CharField(max_length=255)
 location=models.TextField()
 regards=models.CharField(max_length=255)
 tempdata=models.CharField(max_length=200, choices=template_choice)
 created_date=models.DateTimeField(blank=True, default=datetime.now)

 class Meta:
  ordering = ('-id',)