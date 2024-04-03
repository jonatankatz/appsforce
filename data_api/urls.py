from django.urls import path

from . import views

urlpatterns = [
    path('users/read/', views.AllUserListView.as_view(), name='all-user-list'),  
    path('users/create/', views.UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
    path('users/delete/<int:pk>/', views.UserDeleteView.as_view(), name='user-delete'), 
    path('users/update/<int:pk>/', views.UserUpdateView.as_view(), name='user-update'),
    path('departments/read/', views.DepartmentDetailView.as_view(), name='all-department-list'),  
    path('departments/create/', views.DepartmentListCreateView.as_view(), name='department-list-create'),
    path('departments/<int:pk>/', views.DepartmentDetailView.as_view(), name='department-detail'),
    path('departments/delete/<int:pk>/', views.DepartmentDeleteView.as_view(), name='department-delete'), 
    path('departments/update/<int:pk>/', views.DepartmentUpdateView.as_view(), name='department-update'),
    path("departments/with_counts",views.get_departments_with_counts,name="get_departments")
]