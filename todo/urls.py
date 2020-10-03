from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name = "todo"), ## homepage
    path('del/<int:item_id>',views.remove,name = "del"), ## give id no., item id       
]
