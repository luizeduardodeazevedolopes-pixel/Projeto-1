# 🍽️ Sistema de Gerenciamento de Restaurante - Projeto Fatec

Este projeto é um simulador de sistema de gerenciamento desenvolvido para um restaurante fictício localizado próximo à faculdade. Foi criado como parte das atividades acadêmicas da **Fatec Rio Claro - 2º Semestre de 2026**.

O sistema foi construído em Python e aplica conceitos fundamentais de Ciência da Computação, como Estruturas de Dados Customizadas (Listas Encadeadas) e Programação Orientada a Objetos (Herança e Polimorfismo).

## 🚀 Funcionalidades

O sistema orquestra todo o fluxo de um restaurante, incluindo:
- **Gestão de Comandas:** Abertura, adição de itens, cálculo de totais e fechamento.
- **Gestão de Estoque:** Controle de produtos com data de validade, utilizando a lógica de priorizar o lote mais antigo primeiro (FIFO) durante a baixa do estoque.
- **Estruturas de Dados Próprias:** Substituição da lista padrão do Python (`list()`) por uma implementação própria de **Lista Encadeada**.
- **Pagamentos:** Registro de pagamentos validados (PIX, Cartão, Dinheiro).
- **Relatórios:** Geração de relatórios de consumo por cliente e fluxo de vendas (caixa).
- **Persistência de Dados:** Salvamento e carregamento automático do estado completo do restaurante (comandas, estoque, pagamentos) utilizando a biblioteca `pickle`.
- **Simulação Realista:** Uso da biblioteca `Faker` para gerar clientes e consumos aleatórios para testes.

## 🛠️ Tecnologias e Bibliotecas Utilizadas

- **Python 3.x**
- **`datetime`**: Biblioteca nativa utilizada para gerar datas e horários reais (abertura de comandas, vencimento de produtos, hora do pagamento).
- **`pickle`**: Biblioteca nativa utilizada para serialização (salvar e carregar) os objetos do restaurante em um arquivo binário (`restaurante.pkl`).
- **`Faker`**: Biblioteca externa utilizada para popular o sistema com dados falsos e realistas de clientes.

## ⚙️ Como executar o projeto

### 1. Pré-requisitos
Certifique-se de ter o Python instalado na sua máquina. Além disso, você precisará instalar a biblioteca `Faker`.

Abra o terminal e execute o seguinte comando:
```bash
pip install faker
