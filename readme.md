# Blockchain em Python

O meu código é uma implementção simples de uma blockchain.

*Mas o que é uma blockchin afinal?*

Ela é uma cadeia de blocos encadeados por hashes.

## Explicação do código 

No codigo houve duas bibliotecas importadas:

* *hashlib:* 

Biblioteca que fornece funções para criar hashes, como sha-256
* *datetime:* 

Usada para registrar a dat e hora em que o bloco foi criado

### Classe Bloco

A classe Bloco representa um bloco na blockchain.


`def __init__(self, index, data_e_hora, dados, meu_hash):`

| Função | Explicação |
| ---- | ----- |
|index:|Índice do bloco na cadeia.|
|data_e_hora:| Data e hora de criação do bloco.|
|dados: |Informações armazenadas no bloco.|
|meu_hash: |Hash do bloco anterior.|

### Método calcule_hash

`def calcule_hash(self):`

Calcula o hash do bloco atual usando SHA-256, combinando o índice, a data e hora, os dados e o hash do bloco anterior.

### Classe Blockchain

A classe Blockchain representa a cadeia de blocos.



```def __init__(self):```

 ```self.chain = [self.bloco_genesis()]```


Inicializa a blockchain com o bloco gênesis (o primeiro bloco).

### Método bloco_genesis

`def bloco_genesis(self):`

Cria o bloco gênesis com índice 0, data atual, dados "Bloco genesis" e hash "0".

### Método add_bloco

`def add_bloco(self, dados):`

Adiciona um novo bloco à cadeia:
* Calcula o índice do novo bloco.
* Obtém o hash do último bloco.
* Cria um novo bloco com os dados fornecidos.

### Método Validar

`def Validar(self):`

Valida a blockchain verificando se:
* O hash do bloco atual é válido.
* O hash do bloco atual corresponde ao hash do bloco anterior.

### Função Principal

`def main():`

Gerencia a interação do usuário para adicionar blocos à blockchain:
1. Pede dados do item (nome, valor, comprador e vendedor).
2. Adiciona um novo bloco.
3. Valida a blockchain e informa se ela é válida.
4. Pergunta se o usuário deseja adicionar outro bloco.

### Função mostrar_blockchain

`def mostrar_blockchain(chain):`

Exibe todos os blocos na blockchain, mostrando:
* o índice
* data e hora
* dados
* hash 
* hash do bloco anterior

### Execução do Código

` if __name__ == "__main__":`

` main() `

Inicia o programa, chamando a função main.

### Conclusão
Este código fornece uma implementação básica de uma blockchain, demonstrando conceitos fundamentais como hashing, encadeamento de blocos e validação. A estrutura pode ser expandida com funcionalidades adicionais, como tratamento de erros, persistência de dados e segurança.