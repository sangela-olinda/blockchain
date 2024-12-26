import copy
import hashlib
import datetime as date
import secrets
import re

class Bloco:
    def __init__(self, index, data_e_hora, dados, meu_hash, dificuldade=4, minerador=None):
        self.index = index
        self.data_e_hora = data_e_hora
        self.dados = dados
        self.meu_hash = meu_hash
        self.nonce = 0
        self.dificuldade = dificuldade
        self.minerador = minerador  
        self.hash = self.minerar_bloco()

    def calcule_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.index).encode('utf-8') +
                   str(self.data_e_hora).encode('utf-8') +
                   str(self.dados).encode('utf-8') + 
                   str(self.meu_hash).encode('utf-8') +
                   str(self.nonce).encode('utf-8') +
                   str(self.minerador).encode('utf-8'))  
        return sha.hexdigest()

    def minerar_bloco(self):
        while True:
            self.hash = self.calcule_hash()
            if self.hash.startswith('0' * self.dificuldade):
                break
            else:
                self.nonce += 1
        return self.hash

class Transacao:
    def __init__(self, remetente, destinatario, valor, taxa=0):
        self.remetente = remetente
        self.destinatario = destinatario
        self.valor = valor
        self.taxa = taxa  

class Blockchain:
    def __init__(self, dificuldade=4):
        self.dificuldade = dificuldade
        self.chain = [self.bloco_genesis()]
        self.historico_transacoes = {}
        self.saldos = {}  

    def bloco_genesis(self):
        return Bloco(0, date.datetime.now(), "Bloco genesis", "0", self.dificuldade)

    def add_bloco(self, dados, minerador=None):
        index = len(self.chain)
        meu_hash = self.chain[-1].hash
        novo_bloco = Bloco(index, date.datetime.now(), dados, meu_hash, self.dificuldade, minerador)

        self.atualizar_saldo(dados)

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

    def atualizar_saldo(self, dados):
        
        if 'comprador' not in dados or 'valor' not in dados:
            print("Erro: Dados incompletos. Não foi possível atualizar saldo.")
        return
    
        comprador = dados['comprador']
        valor = dados['valor']
    
        if comprador not in self.saldos:
            self.saldos[comprador] = 0
    
        if self.saldos[comprador] < valor:
            print(f"Saldo insuficiente para {comprador}.")
        return
    
        self.saldos[comprador] -= valor

        if comprador not in self.saldos:
            self.saldos[comprador] = 0
    
        if self.saldos[comprador] < valor:
            print(f"Saldo insuficiente para {comprador}. Transação cancelada.")
        return  
    
        self.saldos[comprador] -= valor
        valor = float(dados["Valor"])
        taxa = float(dados.get("Taxa", 0))

        if comprador not in self.saldos:
            self.saldos[comprador] = 0
        if self.saldos[comprador] < valor:
            raise ValueError(f"Saldo insuficiente para o comprador {comprador}")

        self.saldos[comprador] -= valor

        if vendedor not in self.saldos:
            self.saldos[vendedor] = 0
        self.saldos[vendedor] += valor

        if taxa > 0:
            if dados["Minerador"] not in self.saldos:
                self.saldos[dados["Minerador"]] = 0
            self.saldos[dados["Minerador"]] += taxa

    def validar(self):
        for i in range(1, len(self.chain)):
            atual_bloco = self.chain[i]
            proximo_bloco = self.chain[i-1]

            if atual_bloco.hash != atual_bloco.calcule_hash():
                return False
            if atual_bloco.meu_hash != proximo_bloco.hash:
                return False
            
        return True

    def comprimento(self):
        return len(self.chain)

def simular_troca_de_informacoes(nos):

    cadeia_mais_longa = None
    comprimento_maximo = 0

    for no in nos:
        if no.validar() and no.comprimento() > comprimento_maximo:
            cadeia_mais_longa = no.chain
            comprimento_maximo = no.comprimento()

    for no in nos:
        no.chain = copy.deepcopy(cadeia_mais_longa)
    
    print("Sincronização concluída! Todos os nós agora têm a cadeia mais longa válida.")

def endereco_valido(endereco):
    return bool(re.match(r'^2x[a-fA-F0-9]{48}$', endereco))

def gerar_endereco():
    return '2x' + secrets.token_hex(24)  

def main():

    no1 = Blockchain(dificuldade=4)
    no2 = Blockchain(dificuldade=4)
    no3 = Blockchain(dificuldade=4)

    enderecos_existentes = [gerar_endereco() for _ in range(3)]
    print("Endereços gerados:")
    for i, endereco in enumerate(enderecos_existentes):
        print(f"Endereço {i+1}: {endereco}")

    item = input("Digite o item a ser comprado: ")
    valor = input("Digite o valor do item: ")
    taxa = input("Digite a taxa de transação: ")

    print("Selecione o comprador e o vendedor (1, 2 ou 3):")
    comprador = int(input("Comprador (1-3): ")) - 1
    vendedor = int(input("Vendedor (1-3): ")) - 1
    minerador = int(input("Minerador (1-3): ")) - 1

    dados = {
        "Item": item,
        "Valor": valor,
        "Comprador": enderecos_existentes[comprador],
        "Vendedor": enderecos_existentes[vendedor],
        "Taxa": taxa
    }

    no1.add_bloco(dados, enderecos_existentes[minerador])

    simular_troca_de_informacoes([no1, no2, no3])

    print("\n--- Blockchain do nó 1 ---")
    mostrar_blockchain(no1.chain)
    print("\n--- Blockchain do nó 2 ---")
    mostrar_blockchain(no2.chain)
    print("\n--- Blockchain do nó 3 ---")
    mostrar_blockchain(no3.chain)

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
