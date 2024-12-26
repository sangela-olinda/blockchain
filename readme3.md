# Documentação: Blockchain em Python

## Visão Geral
Este código implementa uma simulação de blockchain básica em Python. Ele cria blocos que contêm transações, realiza mineração para encontrar hashes e mantém uma cadeia de blocos segura. Também permite a sincronização de blockchains entre diferentes nós.

## Estrutura do Código

### Importação de Bibliotecas
```python
import copy
import hashlib
import datetime as date
import secrets
import re
```
**Função das Bibliotecas:**
- **copy**: Permite criar cópias profundas da blockchain para sincronização.
- **hashlib**: Usada para calcular o hash SHA-256.
- **datetime**: Manipula datas e horários para os blocos.
- **secrets**: Gera endereços aleatórios.
- **re**: Trabalha com expressões regulares para validação de endereços.

## Classes

### Classe Bloco
```python
class Bloco:
    def __init__(self, index, data_e_hora, dados, meu_hash, dificuldade=4, minerador=None):
```
**Objetivo:**
- Representa um bloco da blockchain.

**Atributos:**
- **index**: Índice do bloco na cadeia.
- **data_e_hora**: Data e hora da criação.
- **dados**: Informações da transação.
- **meu_hash**: Hash do bloco anterior.
- **dificuldade**: Nível de dificuldade para mineração.
- **minerador**: Endereço do minerador que valida o bloco.
- **nonce**: Contador para encontrar o hash correto.

**Métodos:**
- **calcule_hash()**: Calcula o hash do bloco.
- **minerar_bloco()**: Realiza a mineração até que o hash satisfaça a dificuldade.


### Classe Transacao
```python
class Transacao:
    def __init__(self, remetente, destinatario, valor, taxa=0):
```
**Objetivo:**
- Representa uma transação entre um remetente e um destinatário.

**Atributos:**
- **remetente**: Endereço de quem envia.
- **destinatario**: Endereço de quem recebe.
- **valor**: Valor transferido.
- **taxa**: Taxa de transação para o minerador.


### Classe Blockchain
```python
class Blockchain:
    def __init__(self, dificuldade=4):
```
**Objetivo:**
- Representa a cadeia de blocos.

**Atributos:**
- **dificuldade**: Define a dificuldade da mineração.
- **chain**: Lista que armazena os blocos.
- **historico_transacoes**: Armazena o histórico de transações por endereço.
- **saldos**: Dicionário que controla o saldo de cada endereço.

**Métodos:**
- **bloco_genesis()**: Cria o bloco inicial (gênese).
- **add_bloco()**: Adiciona um novo bloco à cadeia após validar o saldo.
- **atualizar_saldo()**: Atualiza o saldo dos envolvidos na transação.
- **validar()**: Verifica se a blockchain é válida.
- **comprimento()**: Retorna o tamanho da blockchain.


## Funções Auxiliares

### Sincronização de Blockchain
```python
def simular_troca_de_informacoes(nos):
```
- Sincroniza as blockchains dos nós envolvidos.
- Copia a blockchain mais longa e válida para os outros nós.


### Geração de Endereços
```python
def gerar_endereco():
```
- Cria endereços de 48 caracteres hexadecimais com prefixo '2x'.


### Validação de Endereço
```python
def endereco_valido(endereco):
```
- Valida o formato do endereço usando expressão regular.


## Função Principal

```python
def main():
```
- Cria três nós de blockchain.
- Gera três endereços aleatórios.
- Solicita ao usuário dados da transação (item, valor, taxa, comprador, vendedor e minerador).
- Adiciona blocos com base nas entradas do usuário.
- Sincroniza a blockchain entre os nós.
- Exibe as blockchains de cada nó.


### Exibição da Blockchain
```python
def mostrar_blockchain(chain):
```
- Exibe informações detalhadas de cada bloco da blockchain.


### Exibição de Transações
```python
def mostrar_historico_transacoes(historico):
```
- Mostra o histórico de transações para cada endereço registrado.


## Execução
```python
if __name__ == "__main__":
    main()
```
- Garante que o código só será executado quando o arquivo for rodado diretamente.

