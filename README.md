# 🍔 Sistema de Restaurante - Fatec Rio Claro

Projeto desenvolvido em Python para simular o gerenciamento de um restaurante universitário, focado em atender os alunos e professores da faculdade. 

**Turma:** Fatec - 2º Semestre de 2026 | Rio Claro - SP.

## 🎯 Objetivo do Projeto
Criar um sistema de controle de comandas, estoque e relatórios de ponta a ponta. Mais do que um simples script, este projeto é um laboratório prático para o estudo aprofundado de **Estruturas de Dados** e **Programação Orientada a Objetos (POO)**.

## 🧠 Conceitos Técnicos Aplicados

Ao invés de utilizar as facilidades prontas da linguagem (como o `list` do Python), o núcleo do sistema foi construído do zero para fins educacionais:

* **Listas Encadeadas (Linked Lists):** Criação manual de uma estrutura de controle de dados através da classe `ListaEncadeada`.
* **Nós (Nodes):** Implementação da classe `No`, funcionando como "vagões" que guardam as informações (cargas) e utilizam ponteiros (`self.proximo`) para se conectar ao restante da fila.
* **Algoritmos de Inserção:** Lógica de varredura (utilizando a estrutura de repetição `while`) para encontrar o último elemento da lista e engatar novos dados de forma dinâmica na memória.
* **Pilares da POO:** Aplicação de Classes, Objetos, Herança, Polimorfismo, Encapsulamento (como o uso de `self._inicio`) e métodos construtores (`__init__`).

## 🛠️ Ferramentas e Bibliotecas Utilizadas

O projeto faz uso de bibliotecas estratégicas para simular um ambiente real:

* **`Faker`**: Biblioteca externa responsável por gerar dados falsos (nomes de clientes fictícios e formas de pagamento sorteadas) para testar o sistema.
* **`datetime`**: Biblioteca nativa do Python utilizada para capturar datas e horários reais das operações (como abertura de comandas e pagamentos).
* **`pickle`**: Biblioteca nativa responsável pela persistência de dados. Ela salva o estado completo do programa em um arquivo `.pkl`, permitindo fechar o código e não perder o histórico do restaurante.

## 🚀 Como Executar

**1. Instale as dependências:**
Como o projeto utiliza o `Faker` para gerar os clientes, é necessário instalá-lo via terminal antes de rodar o código:
```bash
pip install faker
