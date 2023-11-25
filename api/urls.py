from django.urls import path
from . import views

urlpatterns=[
    path('',views.apiOverview),
    path('tasklist',views.itemList),
    path('taskdetail/<str:pk>/',views.itemDetail),
    path('taskcreate',views.itemCreate),
    path('taskupdate/<str:pk>/',views.itemUpdate),
    path('taskdelete/<str:pk>/',views.itemDelete),  
]