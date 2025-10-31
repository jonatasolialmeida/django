from django.db import models


class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField(verbose_name='Preço', decimal_places=2, max_digits=10)
    estoque = models.IntegerField(verbose_name='Quantidade em Estoque')

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('E-mail', max_length=100)
    telefone = models.CharField('Telefone', max_length=100)
    cpf = models.CharField('CPF', max_length=11)
    endereco = models.CharField('Endereco', max_length=100)
    cep = models.CharField('CEP', max_length=7)

    def __str__(self):
        return self.nome