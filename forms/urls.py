from django.urls import path
from . import views
urlpatterns = [
 path('form', views.form,name='form'),
 path('dashboard/<int:id>', views.dashboard,name='dashboard'),
 path('formUpdate/<int:id>', views.formUpdate, name="formUpdate"),
 path('delData/<int:id>', views.delData, name="delData"),
]