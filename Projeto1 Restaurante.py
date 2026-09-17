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


class Bebidas(Consumo_de_Produto):
    TIPOS_BEBIDA = ('Coca Cola', 'Suco', 'Agua')

    def __init__(self, nome, preco):
        # Valida se a bebida é uma das três permitidas pelo enunciado.
        if nome not in Bebidas.TIPOS_BEBIDA:
            raise ValueError(f'Bebida Invalida: {nome}. Opcoes: {Bebidas.TIPOS_BEBIDA}')
        super().__init__(nome, preco)

    def descricao(self):
        return f'[Bebidas] {self.nome} - R$ {self.preco:.2f}'


# Terceira Etapa: Comandas.
# Cada comanda guarda seus próprios itens numa listaencadeada (não numa list),
# tem um estado "aberta/fechada" e sabe calcular seu próprio valor total.
class Comandas:
    def __init__(self, numero, nome_cliente):
        self.numero = numero
        self.nome_cliente = nome_cliente
        self.data_abertura = datetime.now()
        self._itens = listaencadeada()
        self.aberta = True

    def inserir_itens(self, item: Consumo_de_Produto):
        # Regra de negócio: só pode inserir item se a comanda ainda estiver aberta.
        if not self.aberta:
            raise Exception(f'Comanda {self.numero} já está fechada.')
        self._itens.inserir(item)

    def remover_itens(self, nome_item):
        if not self.aberta:
            raise Exception(f'Comanda {self.numero} já está fechada.')
        removido = self._itens.remover(lambda i: i.nome == nome_item)
        if removido is None:
            print(f'Item {nome_item} não encontrado na comanda {self.numero}.')
        return removido

    def valor_total(self):
        # Soma o preço de todos os itens, usando o __iter__ da listaencadeada.
        return sum(item.preco for item in self._itens)

    def itens(self):
        # Converte para list() só na saída, pra facilitar leitura/relatório.
        return list(self._itens)

    def fechar(self):
        self.aberta = False

    def __repr__(self):
        status = 'aberta' if self.aberta else 'fechada'
        return f'Comanda {self.numero} ({self.nome_cliente}, {status}, {len(self._itens)} itens)'


# Quarta Etapa: Estoque.
# "ProdutoEstoque" representa um lote comprado (com data de compra e
# validade). "Estoque" guarda vários lotes numa listaencadeada e sabe
# baixar quantidade priorizando sempre o lote mais antigo primeiro.
class ProdutoEstoque:
    def __init__(self, nome, preco_compra, preco_venda, data_compra, data_vencimento, quantidade):
        self.nome = nome
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda   # <- adicionado: o enunciado pede compra E venda
        self.data_compra = data_compra
        self.data_vencimento = data_vencimento
        self.quantidade = quantidade

    def __repr__(self):
        data_formatada = self.data_vencimento.strftime('%d/%m/%Y')
        return f'{self.nome} (qtd={self.quantidade}, venc={data_formatada})'


class Estoque:
    def __init__(self):
        self._produtos = listaencadeada()

    def adicionar_produto(self, produto: ProdutoEstoque):
        self._produtos.inserir(produto)

    def baixar_estoque(self, nome_produto, quantidade):
        """
        Baixa a quantidade do produto, priorizando o lote com data de
        compra mais antiga (produtos mais velhos são usados primeiro).
        """
        candidatos = [p for p in self._produtos if p.nome == nome_produto and p.quantidade > 0]
        candidatos.sort(key=lambda p: p.data_compra)  # mais antigo primeiro

        restante = quantidade
        for produto in candidatos:
            if restante <= 0:
                break
            usado = min(produto.quantidade, restante)
            produto.quantidade -= usado
            restante -= usado

        if restante > 0:
            raise Exception(f"Estoque insuficiente de '{nome_produto}'. Faltaram {restante} unidade(s).")

    def editar_quantidade(self, nome_produto, nova_quantidade):
        produto = self._produtos.buscar(lambda p: p.nome == nome_produto)
        if produto is None:
            raise Exception(f"Produto '{nome_produto}' não encontrado no estoque.")
        produto.quantidade = nova_quantidade

    def listar(self):
        return list(self._produtos)


# Quinta Etapa: Pagamento.
# Guarda quem pagou, de qual comanda, a forma de pagamento (validada) e o valor,
# com data/hora automática no momento da criação.
class Pagamento:
    FORMAS_VALIDAS = ('PIX', 'Cartão', 'Dinheiro')

    def __init__(self, nome_cliente, numero_comanda, forma_pagamento, valor_total):
        if forma_pagamento not in Pagamento.FORMAS_VALIDAS:
            raise ValueError(f'Forma de pagamento invalida: {forma_pagamento}')
        self.nome_cliente = nome_cliente
        self.numero_comanda = numero_comanda
        self.forma_pagamento = forma_pagamento
        self.valor_total = valor_total
        self.data_hora = datetime.now()

    def __repr__(self):
        return (f'Pagamento comanda {self.numero_comanda} | {self.nome_cliente} | '
                f'{self.forma_pagamento} | R$ {self.valor_total:.2f}')


# Sexta Etapa: Restaurante (classe orquestradora).
# Junta comandas abertas, histórico, estoque e pagamentos, e concentra o
# fluxo completo de atendimento: abrir comanda, fechar comanda (baixando
# estoque e gerando pagamento) e manter tudo organizado.
class Restaurante:
    def __init__(self):
        self.comandas_abertas = listaencadeada()
        self.historico_comandas = listaencadeada()
        self.estoque = Estoque()
        self.pagamentos = listaencadeada()
        self._proximo_numero = 1

    def abrir_comanda(self, nome_cliente):
        comanda = Comandas(self._proximo_numero, nome_cliente)
        self._proximo_numero += 1
        self.comandas_abertas.inserir(comanda)
        return comanda

    def fechar_comanda(self, numero_comanda, forma_pagamento):
        comanda = self.comandas_abertas.buscar(lambda c: c.numero == numero_comanda)
        if comanda is None:
            raise Exception(f'Comanda {numero_comanda} não encontrada entre as abertas.')

        # baixa o estoque de cada item consumido (1 unidade por item, por simplicidade)
        for item in comanda.itens():
            self.estoque.baixar_estoque(item.nome, 1)

        comanda.fechar()
        valor = comanda.valor_total()
        pagamento = Pagamento(comanda.nome_cliente, comanda.numero, forma_pagamento, valor)
        self.pagamentos.inserir(pagamento)

        self.comandas_abertas.remover(lambda c: c.numero == numero_comanda)
        self.historico_comandas.inserir(comanda)
        return pagamento


# Sétima Etapa: Geração de dados fake (Faker) e persistência (pickle).
def povoar_estoque(restaurante: Restaurante):
    """Cadastra alguns produtos fixos de estoque para a simulação."""
    hoje = datetime.now()
    restaurante.estoque.adicionar_produto(
        ProdutoEstoque('Prato Feito', 8.0, 25.0, hoje, hoje.replace(day=28), 50)
    )
    restaurante.estoque.adicionar_produto(
        ProdutoEstoque('Coca Cola', 2.0, 6.0, hoje, hoje.replace(day=28), 100)
    )
    restaurante.estoque.adicionar_produto(
        ProdutoEstoque('Suco', 1.5, 6.0, hoje, hoje.replace(day=28), 80)
    )
    restaurante.estoque.adicionar_produto(
        ProdutoEstoque('Agua', 1.0, 4.0, hoje, hoje.replace(day=28), 100)
    )


def gerar_dados_fake(restaurante: Restaurante, quantidade_clientes=5):
    """Usa a biblioteca Faker para simular clientes entrando no restaurante."""
    fake = Faker('pt_BR')
    bebidas_disponiveis = list(Bebidas.TIPOS_BEBIDA)

    for _ in range(quantidade_clientes):
        comanda = restaurante.abrir_comanda(fake.name())
        comanda.inserir_itens(Refeicoes('Prato Feito', 25.0))
        bebida_sorteada = fake.random_element(elements=bebidas_disponiveis)
        comanda.inserir_itens(Bebidas(bebida_sorteada, 6.0))


def salvar_dados(restaurante: Restaurante, caminho='restaurante.pkl'):
    with open(caminho, 'wb') as arquivo:
        pickle.dump(restaurante, arquivo)
    print(f"Dados salvos em '{caminho}'.")


def carregar_dados(caminho='restaurante.pkl') -> Restaurante:
    with open(caminho, 'rb') as arquivo:
        return pickle.load(arquivo)


# Oitava Etapa: Relatórios de vendas e de consumo.
def relatorio_vendas(restaurante: Restaurante):
    print('\n=== RELATÓRIO DE VENDAS ===')
    total = sum(p.valor_total for p in restaurante.pagamentos)
    for pagamento in restaurante.pagamentos:
        print(f'- {pagamento}')
    print(f'TOTAL ARRECADADO: R$ {total:.2f}')


def relatorio_consumo(restaurante: Restaurante):
    print('\n=== RELATÓRIO DE CONSUMO ===')
    for comanda in restaurante.historico_comandas:
        print(f'{comanda.nome_cliente} (Comanda {comanda.numero}):')
        for item in comanda.itens():
            print(f'   {item.descricao()}')


# Nona Etapa: Simulação completa de um dia de atendimento.
if __name__ == '__main__':
    restaurante = Restaurante()
    povoar_estoque(restaurante)
    gerar_dados_fake(restaurante, quantidade_clientes=5)

    # Fecha todas as comandas abertas com uma forma de pagamento aleatória
    fake = Faker('pt_BR')
    formas = list(Pagamento.FORMAS_VALIDAS)
    numeros_abertos = [c.numero for c in restaurante.comandas_abertas]

    for numero in numeros_abertos:
        forma = fake.random_element(elements=formas)
        restaurante.fechar_comanda(numero, forma)

    relatorio_vendas(restaurante)
    relatorio_consumo(restaurante)

    salvar_dados(restaurante)
    restaurante_recarregado = carregar_dados()
    print('\nDados recarregados com sucesso do pickle!')
    relatorio_vendas(restaurante_recarregado)


    






