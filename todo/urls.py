from django.urls import path 
from . import views 


urlpatterns=[
    path ('addTask/',views.addTask ,name='addTask'),
    # path('addTask/', views.addTask, name='addTask'),
    # mark as done
    path ('mark_as_done/<int:pk>/',views.mark_as_done ,name='mark_as_done'),
    
    # mark as done
    path ('mark_as_undone/<int:pk>/',views.mark_as_undone ,name='mark_as_undone'),
    
    # edit
    path ('edit_task/<int:pk>/',views.edit_task, name='edit_task'),

    # delete
    path ('delete/<int:pk>/',views.delete, name='delete'),


]