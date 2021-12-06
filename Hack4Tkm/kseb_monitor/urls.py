from django.urls import path
from .views import index, predict,update,dataplot
urlpatterns = [
    path('',index,name='kseb_monitor'),
    path('update/',update,name='update'),
    path('predict/',predict,name='predict'),
    path('dataplot/',dataplot,name='dataplot'),

]