from django.urls import path

from admins.views import index, UserListView, UserCreateView, UserAdminUpdateView, UserAdminDeleteView, \
    categories, ProductCategoryUpdateView, category_create

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('users-create/', UserCreateView.as_view(), name='admin_users_create'),
    path('users-update/<int:pk>/', UserAdminUpdateView.as_view(), name='admin_users_update'),
    path('users-delete/<int:pk>/', UserAdminDeleteView.as_view(), name='admin_users_delete'),
    #
    path('categories/create/', category_create, name='category_create'),
    path('categories/read/', categories, name='categories'),
    path('categories/update/<int:pk>/', ProductCategoryUpdateView.as_view(), name='category_update'),
    #path('categories/delete/<int:pk>/', category_delete, name='category_delete'),
]
