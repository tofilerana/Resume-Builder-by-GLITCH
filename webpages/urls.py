from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name='index'),
    
    path('detailedView/<int:id>', views.detailedView,name='detailedView'),
    path('click/<int:id>', views.click,name='click'),
    # path('click2/<int:id>', views.click2,name='click2'),
]