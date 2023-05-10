from django.urls import path 
from app import views
urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('<int:id>',views.edit,name='edit'),
]
