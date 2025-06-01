from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Produto, Cliente, Venda
from .forms import ProdutoForm, ClienteForm, VendaForm

# Listagem
def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/list.html', {'produtos': produtos})

def lista_Cliente(request):
    clientes = Cliente.objects.all()
    return render(request, 'produtos/lista_clientes.html', {'clientes': clientes})


# =============

def lista_vendas(request):
    cliente_id = request.GET.get('clientes')
    data_inicio = request.GET.get('data_inicio')
    data_fim = request.GET.get('data_fim')

    vendas = Venda.objects.all()

    if cliente_id:
        vendas = vendas.filter(cliente_id=cliente_id)

    if data_inicio and data_fim:
        vendas = vendas.filter(data_venda__range=[data_inicio, data_fim])

    return render(request, 'produtos/lista_vendas.html', {'vendas': vendas})

# =============

# Criação
def cria_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'produtos/form.html', {'form': form})

def cria_Cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_Cliente')
    else:
        form = ClienteForm()
    return render(request, 'produtos/cliente_form.html', {'form': form})

# =============

def cria_venda(request):
    if request.method == 'POST':
        form = VendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_vendas')
    else:
        form = VendaForm()
    return render(request, 'produtos/venda_form.html', {'form': form})

# =============

# Edição
def edita_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produtos/form.html', {'form': form})

def edita_Cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    form = ClienteForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect('lista_Cliente')
    return render(request, 'produtos/cliente_form.html', {'form': form})

# =============

def edita_venda(request, pk):
    venda = get_object_or_404(Venda, pk=pk)
    form = VendaForm(request.POST or None, instance=venda)
    if form.is_valid():
        form.save()
        return redirect('lista_vendas')
    return render(request, 'produtos/venda_form.html', {'form': form})

# =============

# Remoção
def remove_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        produto.delete()
        return redirect('lista_produtos')
    return render(request, 'produtos/confirm_delete.html', {'produto': produto})

def remove_Cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('lista_Cliente')
    return render(request, 'produtos/cliente_confirm_delete.html', {'cliente': cliente})

# =============

def remove_venda(request, pk):
    venda = get_object_or_404(Venda, pk=pk)
    if request.method == 'POST':
        venda.delete()
        return redirect('lista_vendas')
    return render(request, 'produtos/venda_confirm_delete.html', {'venda': venda})

# =============