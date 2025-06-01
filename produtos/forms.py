from django.forms import ModelForm
from .models import Produto, Cliente, Venda

class ProdutoForm(ModelForm):
    class Meta: # armazena metadados
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'estoque']

class ClienteForm(ModelForm): #criando formulário
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'nascimento']

class VendaForm(ModelForm):
    class Meta:
        model = Venda
        fields = ['cliente', 'produto', 'quantidade']