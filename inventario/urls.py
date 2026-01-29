from django.urls import path
from . import views

urlpatterns = [
    path('material/', views.material_list, name='material_list'),
    path('material/novo/', views.material_create, name='material_create'),
    path('material/<int:pk>/', views.material_detail, name='material_detail'),
    path('material/<int:pk>/editar', views.material_update, name='material_update'),
    path('material/<int:pk>/excluir', views.material_delete, name='material_delete')
]
