# Blockchain em Python

Este é um exemplo de implementação básica de uma blockchain com funcionalidades adicionais, como Proof of Work, validação de endereços e histórico de transações por endereço.

**O que é uma blockchain?**

Blockchain é uma cadeia de blocos interligados por hashes, onde cada bloco armazena informações e se refere ao anterior, garantindo a integridade da cadeia.

---

## Explicação do Código

### Bibliotecas Usadas

O código usa as bibliotecas:

* `hashlib`: Funções para criar hashes (ex. SHA-256).
* `datetime`: Usada para registrar data e hora de criação do bloco.

### Classe `Bloco`

A classe `Bloco` representa cada bloco na blockchain e inclui o índice, data e hora, dados de transação, hash do bloco anterior, nonce e dificuldade para Proof of Work.

#### Construtor

```python
def __init__(self, index, data_e_hora, dados, meu_hash, dificuldade=2):
```

| Parâmetro      | Explicação                                                 |
|----------------|------------------------------------------------------------|
| `index`        | Índice do bloco na cadeia                                  |
| `data_e_hora`  | Data e hora de criação do bloco                            |
| `dados`        | Informações armazenadas no bloco                           |
| `meu_hash`     | Hash do bloco anterior                                     |
| `dificuldade`  | Nível de dificuldade para o Proof of Work (padrão: 2)      |

#### Método `calcule_hash`

Calcula o hash do bloco atual combinando o índice, data, dados, hash anterior e nonce, garantindo que o hash identifica o bloco de forma única.

```python
def calcule_hash(self):
```

#### Método `minerar_bloco`

Implementa o **Proof of Work (PoW)** ajustando o nonce até que o hash comece com o número de zeros determinado por `dificuldade`.

```python
def minerar_bloco(self):
```

---

### Classe `Blockchain`

A classe `Blockchain` representa a cadeia de blocos, incluindo validação, adição de blocos, geração de endereços e histórico de transações.

#### Construtor

```python
def __init__(self, dificuldade=2):
```

Inicializa a blockchain com o bloco gênesis e configura a dificuldade para o PoW. Também cria o histórico de transações para registrar todas as transações associadas a cada endereço.

#### Método `bloco_genesis`

Cria o bloco gênesis (primeiro bloco) com índice 0, data atual, dados "Bloco genesis" e hash "0".

```python
def bloco_genesis(self):
```

#### Método `add_bloco`

Adiciona um novo bloco à blockchain:

* Calcula o índice do novo bloco.
* Obtém o hash do último bloco.
* Cria um novo bloco com os dados fornecidos.
* Atualiza o histórico de transações com os endereços do comprador e vendedor.

```python
def add_bloco(self, dados):
```

#### Método `validar`

Valida a blockchain verificando:

* Consistência do hash de cada bloco.
* Correspondência entre o hash do bloco anterior e o hash registrado no bloco seguinte.

```python
def validar(self):
```

---

### Funções Auxiliares

#### Validação e Geração de Endereços

* `endereco_valido(endereco)`: Valida o formato de um endereço (ex. deve começar com "2x" e ter 48 caracteres hexadecimais).
* `gerar_endereco()`: Gera um novo endereço com o formato correto.

#### Seleção de Endereços

* `selecionar_endereco(enderecos_existentes)`: Permite ao usuário escolher um endereço existente ou gerar um novo. Permite a reutilização de endereços para múltiplas transações.

---

### Função Principal (`main`)

Gerencia a interação do usuário para adicionar blocos à blockchain:

1. Pede dados do item (nome, valor, comprador e vendedor).
2. Permite escolher ou gerar endereços para comprador e vendedor.
3. Adiciona um novo bloco à blockchain.
4. Valida a blockchain e informa se ela é válida.
5. Exibe a blockchain e o histórico de transações por endereço ao final.

```python
def main():
```

---

### Exibição da Blockchain

Exibe todos os blocos na blockchain com o índice, data e hora de criação, dados de transação, hash do bloco e do bloco anterior, e o nonce usado para PoW.

```python
def mostrar_blockchain(chain):
```

### Exibição do Histórico de Transações

Exibe o histórico de transações por endereço, mostrando:

* Dados de cada transação associada ao endereço.
* Bloco em que a transação ocorreu.
* Hash do bloco.

```python
def mostrar_historico_transacoes(historico):
```

---

### Execução do Código

```python
if __name__ == "__main__":
    main()
```

Inicia o programa chamando a função `main()`.

---

## Conclusão

Este código oferece uma implementação simples de uma blockchain com funcionalidades para aplicações como lojas ou mercados. Inclui:

- **Proof of Work (PoW)** para mineração
- **Validação de Endereços** para compradores e vendedores
- **Reutilização de Endereços** para múltiplas transações
- **Histórico de Transações por Endereço**, permitindo rastrear todas as atividades de um comprador ou vendedor