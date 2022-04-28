from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'todoapp'
urlpatterns = [
    path('login/', views.TodoLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='todoapp:login'), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),

    path('', views.TodoListView.as_view(), name='index'),
    path('task/<int:pk>/', views.TodoDetailView.as_view(), name='detail'),
    path('task-create/', views.TodoCreateView.as_view(), name='task-create'),
    path('task-update/<int:pk>', views.TodoUpdateView.as_view(), name='task-update'),
    path('task-delete/<int:pk>', views.TodoDeleteView.as_view(), name='task-delete'),
    
]   