#projeto1-restaurante proximo a faculdade fatec.
#Fatec Segundo Semestre-2026, Fatec Rio Claro.
#Ferramentas utilizadas:
#-Faker:gera dados falsos precisa ser importado.
#-pickle:será utilizado para executar o arquivo dentro da pasta Restaurante.
#-datetime:é uma biblioteca nativa do proprio python que gera datas e horarios rais.

from datetime import datetime
import pickle
from faker import Faker

# Agora iremos criar uma classe e apos isso uma lista encadeada.
# abaixo está a classe No que foi criada

# Primeira Etapa: Criação do Nó e Lista Encadeada.
# O "No" é a unidade básica: guarda uma informação e aponta para o próximo nó.
# A "listaencadeada" usa vários "No" conectados entre si, no lugar de usar
# a list() pronta do Python, já que o enunciado pede estrutura própria.
class No:
    # Apos a classe No ser criada dei inicio a lista encadeada
    def __init__(self, informacao):
        self.informacao = informacao   # o dado guardado nesse nó
        self.proximo = None            # referência para o próximo nó (None = fim da lista)


class listaencadeada:
    def __init__(self):
        self._inicio = None   # referência para o primeiro nó da lista
        self.tamanho = 0       # contador de quantos nós existem

    def inserir(self, informacao):
        # Cria um novo nó e o encaixa no final da lista.
        novo_no = No(informacao)
        if self._inicio is None:
            self._inicio = novo_no
        else:
            atual = self._inicio
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_no
        self.tamanho += 1

    def remover(self, condicao):
        # Percorre a lista guardando o nó "anterior" ao atual, para poder
        # reconectar a lista quando o nó procurado for encontrado e removido.
        anterior = None
        atual = self._inicio
        while atual is not None:
            if condicao(atual.informacao):
                if anterior is None:
                    self._inicio = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                self.tamanho -= 1
                return atual.informacao
            anterior = atual
            atual = atual.proximo
        return None

    def buscar(self, condicao):
        # Igual ao remover, mas só localiza e devolve o dado, sem tirar da lista.
        atual = self._inicio
        while atual is not None:
            if condicao(atual.informacao):
                return atual.informacao
            atual = atual.proximo
        return None

    def __iter__(self):
        # Permite usar "for item in minha_lista" normalmente.
        atual = self._inicio
        while atual is not None:
            yield atual.informacao
            atual = atual.proximo

    def __len__(self):
        # Permite usar len(minha_lista).
        return self.tamanho


# Segunda Etapa: Produtos (Refeições e Bebidas) — Herança e Polimorfismo.
# "Consumo_de_Produto" é a classe-mãe com o que é comum a qualquer item
# consumido (nome e preço). "Refeicoes" e "Bebidas" herdam dela e cada
# uma sobrescreve descricao() do seu próprio jeito (polimorfismo).
class Consumo_de_Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def descricao(self):
        return f'{self.nome} - R$ {self.preco:.2f}'

    def __repr__(self):
        return self.descricao()


class Refeicoes(Consumo_de_Produto):
    def descricao(self):
        return f'[Refeições] {self.nome} - R$ {self.preco:.2f}'


    






