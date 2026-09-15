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
#abaixo está a classe No que foi criada
class No:
#Apos a classe No ser criada dei inicio a lista encadeada
        def __init__(self,informacao):
        self.informacao = informacao
        self.proximo = None
class listaencadeada:
    def __init__(self):
        self._inicio = None
        self.tamanho = 0

    def inserir(self,informacao):
        novo_no = No(informacao)
        if self._inicio == None:
            self._inicio = novo_no

        else:
            atual = self._inicio
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_no
        self.tamanho += 1

    






