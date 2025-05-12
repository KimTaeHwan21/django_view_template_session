from django.urls import path
from .views import index, show, create, edit, update, delete, create_comment, delete_comment

app_name = 'article'

urlpatterns = [
    path('', index, name = 'index'),
    path('<int:pk>', show, name = 'show'),
    # path('new/', new, name = 'new'),
    path('create/', create, name = 'create'),
    path('<int:pk>/edit', edit, name = 'edit'),
    path('<int:pk>/update', update, name = 'update'),
    path('<int:pk>/delete', delete, name = 'delete'),

    path('<int:pk>/comments/create/', create_comment, name='create_comment'),
    path('comment/<int:comment_pk>/delete/', delete_comment, name='delete_comment'),

]