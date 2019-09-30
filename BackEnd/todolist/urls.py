from django.urls import path,include
# from django.contrib.auth import views as auth_views
from . import views

app_name = 'todolist'

urlpatterns = [
    path('logout/', views.logout_view, name='logout'),
    path('index/', views.index, name='index'),
    path('<int:todo_id>', views.tododetail, name='detail'),
    path('create/', views.create_todo, name='create'),
    path('delete/<int:todo_id>', views.delete_todo, name='delete'),
    path('update/<int:todo_id>', views.update_todo, name='update'),
    path('<int:todo_id>/updateitem/<int:item_id>', views.update_item, name='updateitem'),
    path('<int:todo_id>/deleteitem/<int:item_id>', views.delete_item, name='deleteitem'),
    path('createitem/<int:todo_id>', views.create_item, name='createitem'),
    path('', views.loginview, name='loginview'),
]