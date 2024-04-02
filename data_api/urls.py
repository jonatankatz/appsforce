from django.urls import path

from . import views

urlpatterns = [
    path('users/', views.UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
    path('users/all/', views.AllUserListView.as_view(), name='all-user-list'),  
    path('users/delete/<int:pk>/', views.UserDeleteView.as_view(), name='user-delete'), 
    path('users/update/<int:pk>/', views.UserUpdateView.as_view(), name='user-update'), 
    path("departments/with_counts",views.get_departments_with_counts,name="get_departments")
]