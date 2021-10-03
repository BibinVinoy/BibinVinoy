from django.urls import path
from . import views

app_name='todo'
urlpatterns=[
    path('',views.home),
    path('delete/<int:id>/',views.delete),
    path('update/<int:id>/',views.update),
    path('listview/',views.TaskListView.as_view(),name='listview'),
    path('detailview/<int:pk>/',views.TaskDetailView.as_view(),name='TaskDetaiView'),
    path('updateview/<int:pk>/',views.TaskUpdateView.as_view(),name='TaskUpdateView'),
    path('deleteview/<int:pk>/',views.TaskDeleteView.as_view(),name='TaskDeleteView')
]