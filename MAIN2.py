import hashlib
import datetime as date
import secrets
import re

class Bloco:
    def __init__(self, index, data_e_hora, dados, meu_hash, dificuldade=4):
        self.index = index
        self.data_e_hora = data_e_hora
        self.dados = dados
        self.meu_hash = meu_hash
        self.nonce = 0
        self.dificuldade = dificuldade
        self.hash = self.minerar_bloco()

    def calcule_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.index).encode('utf-8') +
                   str(self.data_e_hora).encode('utf-8') +
                   str(self.dados).encode('utf-8') + 
                   str(self.meu_hash).encode('utf-8') +
                   str(self.nonce).encode('utf-8'))
        return sha.hexdigest()

    def minerar_bloco(self):
        while True:
            self.hash = self.calcule_hash()
            if self.hash.startswith('0' * self.dificuldade):
                break
            else:
                self.nonce += 1
        return self.hash

class Blockchain:
    def __init__(self, dificuldade=4):
        self.dificuldade = dificuldade
        self.chain = [self.bloco_genesis()]
        self.historico_transacoes = {}

    def bloco_genesis(self):
        return Bloco(0, date.datetime.now(), "Bloco genesis", "0", self.dificuldade)

    def add_bloco(self, dados):
        index = len(self.chain)
        meu_hash = self.chain[-1].hash
        novo_bloco = Bloco(index, date.datetime.now(), dados, meu_hash, self.dificuldade)
        self.chain.append(novo_bloco)
        
        for endereco in [dados["Comprador"], dados["Vendedor"]]:
            if endereco not in self.historico_transacoes:
                self.historico_transacoes[endereco] = []
            self.historico_transacoes[endereco].append({
                "Bloco": index,
                "Data e Hora": novo_bloco.data_e_hora,
                "Dados": dados,
                "Hash": novo_bloco.hash
            })

    def validar(self):
        for i in range(1, len(self.chain)):
            atual_bloco = self.chain[i]
            proximo_bloco = self.chain[i-1]

            if atual_bloco.hash != atual_bloco.calcule_hash():
                return False
            if atual_bloco.meu_hash != proximo_bloco.hash:
                return False
            
        return True

def endereco_valido(endereco):
    return bool(re.match(r'^2x[a-fA-F0-9]{48}$', endereco))

def gerar_endereco():
    return '2x' + secrets.token_hex(24)  # 48 caracteres hexadecimais

def selecionar_endereco(enderecos_existentes):
    print("\nEndereços disponíveis:")
    for idx, endereco in enumerate(enderecos_existentes):
        print(f"{idx + 1}. {endereco}")
    print(f"{len(enderecos_existentes) + 1}. Gerar novo endereço")
    
    escolha = int(input("Escolha um endereço para usar (número): "))
    if escolha == len(enderecos_existentes) + 1:
        novo_endereco = gerar_endereco()
        print("Novo endereço gerado:", novo_endereco)
        return novo_endereco
    else:
        return enderecos_existentes[escolha - 1]

def main():
    minha_blockchain = Blockchain(dificuldade=4)
    enderecos_existentes = []

    while True:
        print("\nAdicionar um novo bloco")

        item = input("Digite o nome do item: ")
        valor = input("Digite o valor do item: ")

        if enderecos_existentes:
            comprador = selecionar_endereco(enderecos_existentes)
            vendedor = selecionar_endereco(enderecos_existentes)
        else:
            comprador = gerar_endereco()
            vendedor = gerar_endereco()
            enderecos_existentes.extend([comprador, vendedor])

        print("Endereço do Comprador selecionado:", comprador)
        print("Endereço do Vendedor selecionado:", vendedor)

        dados = {
            "Item": item,
            "Valor": valor,
            "Comprador": comprador,
            "Vendedor": vendedor
        }

        minha_blockchain.add_bloco(dados)

        if minha_blockchain.validar():
            print("A blockchain é válida.")
        else:
            print("A blockchain não é válida!")

        continuar = input("Deseja adicionar outro bloco? (sim ou nao): ")
        if continuar.lower() != 'sim':
            break

    mostrar_blockchain(minha_blockchain.chain)
    mostrar_historico_transacoes(minha_blockchain.historico_transacoes)

def mostrar_blockchain(chain):
    print("\n--- Blockchain ---")
    for bloco in chain:
        print(f"Bloco: {bloco.index}")
        print(f"Data e Hora: {bloco.data_e_hora}")
        print(f"Dados: {bloco.dados}")
        print(f"Hash: {bloco.hash}")
        print(f"Nonce: {bloco.nonce}")
        print(f"Hash do bloco anterior: {bloco.meu_hash if bloco.index > 0 else 'N/A'}")
        print(25 * "-----")

def mostrar_historico_transacoes(historico):
    print("\n--- Histórico de Transações por Endereço ---")
    for endereco, transacoes in historico.items():
        print(f"\nEndereço: {endereco}")
        for transacao in transacoes:
            print(f"  Bloco: {transacao['Bloco']}")
            print(f"  Data e Hora: {transacao['Data e Hora']}")
            print(f"  Dados: {transacao['Dados']}")
            print(f"  Hash: {transacao['Hash']}")
            print(15 * "-----")

if __name__ == "__main__":
    main()
