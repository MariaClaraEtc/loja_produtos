from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    estoque = models.PositiveIntegerField()

    def __str__(self):
        return self.nome

class Cliente(models.Model): #modelo Cliente
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    nascimento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome
    
class Venda(models.Model): #modelo Vendaa
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    data_venda = models.DateField(auto_now_add=True)

    def valor_total(self):
        return self.produto.preco * self.quantidade
    
    def __str__(self):
        return f"{self.cliente.nome} - {self.produto.nome} ({self.quantidade})"