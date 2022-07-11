from django.urls import path 
from main import views

urlpatterns = [
    path('',views.addshow,name='home'),
    path('/delete/<int:id>',views.delete1,name='delete'),
    path('/update/<int:id>',views.update1,name='update'),


]
