from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),
    path('novo/', views.cria_produto, name='cria_produto'),
    path('edita/<int:pk>/', views.edita_produto, name='edita_produto'),
    path('remove/<int:pk>/', views.remove_produto, name='remove_produto'),
    # ==========================================================
    path('clientes/', views.lista_Cliente, name='lista_Cliente'),
    path('clientes/novo/', views.cria_Cliente, name='cria_Cliente'),
    path('clientes/<int:pk>/editar/', views.edita_Cliente, name='edita_Cliente'),
    path('clientes/<int:pk>/excluir/', views.remove_Cliente, name='remove_Cliente'),
    # ==========================================================
    path('vendas/', views.lista_vendas, name='lista_vendas'),
    path('vendas/novo/', views.cria_venda, name='cria_venda'),
    path('vendas/<int:pk>/editar/', views.edita_venda, name='edita_venda'),
    path('vendas/<int:pk>/excluir/', views.remove_venda, name='remove_venda'),
]