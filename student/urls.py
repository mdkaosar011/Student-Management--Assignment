from django.contrib import admin
from django.urls import path

from student import views

urlpatterns = [
    path('', views.StudentListView.as_view(), name = 'home'),
    path('addnew/', views.AddNew.as_view(), name= 'addnew'),
    path('update/<int:sID>/', views.Update.as_view(), name='update'),
    path('delete/<int:sID>/', views.Delete.as_view(), name='delete'),
    path('search/', views.Search.as_view(), name='search'),
]
