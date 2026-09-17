# Projeto Restaurante - Fatec Rio Claro

**Projeto 1 - Sistema de Restaurante próximo à Faculdade FATEC**  
*Fatec Rio Claro - Segundo Semestre de 2026*

## 📖 Sobre o Projeto

Este projeto consiste em um sistema em Python para gerenciar o consumo em um restaurante localizado próximo à Fatec. O diferencial deste projeto é a implementação manual de estruturas de dados (Listas Encadeadas) e o uso prático de conceitos de Programação Orientada a Objetos (POO), como Herança e Polimorfismo, em vez de depender apenas de estruturas prontas.

## 🚀 Funcionalidades e Estrutura do Código

O código atual está dividido nas seguintes etapas focadas em fundamentos da computação:

### 1. Estrutura de Dados Customizada (Lista Encadeada)
Em vez de utilizar as listas nativas do Python (`list()`), foi criada uma estrutura própria baseada em nós (`No` e `listaencadeada`). Ela suporta operações fundamentais como:
*   `inserir()`: Encaixa um novo nó ao final da lista.
*   `remover()`: Localiza e reconecta a lista após remover um elemento baseado em uma condição.
*   `buscar()`: Localiza um elemento sem retirá-lo da lista.
*   **Métodos mágicos:** Suporte a iteração nativa (`__iter__`) para loops `for` e contagem (`__len__`) para `len()`.

### 2. POO: Herança e Polimorfismo
O catálogo de produtos do restaurante foi modelado utilizando herança:
*   `Consumo_de_Produto`: Classe-mãe que define atributos comuns a qualquer item consumido (nome e preço) e fornece uma descrição padrão.
*   `Refeicoes` e `Bebidas`: Classes filhas que herdam de `Consumo_de_Produto`. Elas demonstram **polimorfismo** ao sobrescrever o método `descricao()` para exibir formatações específicas (ex: `[Refeições] Nome - R$ 0.00`).

## 🛠️ Ferramentas e Bibliotecas Utilizadas

*   **[Faker](https://faker.readthedocs.io/):** Biblioteca externa utilizada para a geração rápida e aleatória de dados fictícios.
*   **Pickle:** Biblioteca nativa do Python, utilizada para serialização de objetos (salvar e carregar dados estruturados diretamente da pasta do Restaurante).
*   **Datetime:** Biblioteca nativa para manipulação de datas e horários reais (útil para registrar horário de consumo e operações).

## ⚙️ Pré-requisitos

Para rodar este projeto, você precisará do **Python 3.x** instalado em sua máquina, além da instalação das bibliotecas externas listadas.

1. Instale o Faker utilizando o pip:
```bash
pip install faker
```

## 🏃‍♂️ Como Executar

1. Clone ou faça o download deste diretório.
2. Certifique-se de que o pacote `faker` está instalado no seu ambiente.
3. Execute o script principal do projeto no seu terminal:
```bash
python nome_do_arquivo.py
```

---
*Desenvolvido para fins acadêmicos - Fatec Rio Claro.*
