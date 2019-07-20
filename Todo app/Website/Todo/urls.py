
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name='Home'),
    path('add/',views.newtodo,name='newtodo'),
    path('complete/int:<todo_id>', views.addtodo, name='add'),
    path('delete/', views.deletetodo, name='delete'),
    path('deleteall/',views.deleteall,name='deleteall')
    
]