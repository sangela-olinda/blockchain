import hashlib
import datetime as date

class Bloco:
    def __init__(self, index, data_e_hora, dados, meu_hash):
        self.index = index
        self.data_e_hora = data_e_hora
        self.dados = dados
        self.meu_hash = meu_hash
        self.hash = self.calcule_hash()

    def calcule_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.index).encode('utf-8') +
                   str(self.data_e_hora).encode('utf-8') +
                   str(self.dados).encode('utf-8') + 
                   str(self.meu_hash).encode('utf-8'))
        return sha.hexdigest()
    
class Blockchain:
    def __init__(self):
        self.chain = [self.bloco_genesis()]

    def bloco_genesis(self):
        return Bloco(0, date.datetime.now(), "Bloco genesis", "0")

    def add_bloco(self, dados):
        index = len(self.chain)
        meu_hash = self.chain[-1].hash
        novo_bloco = Bloco(index, date.datetime.now(), dados, meu_hash)
        self.chain.append(novo_bloco)

    def Validar(self):
        for i in range(1, len(self.chain)):
            atual_bloco = self.chain[i]
            proximo_bloco = self.chain[i-1]

            if atual_bloco.hash != atual_bloco.calcule_hash():
                return False
            if atual_bloco.meu_hash != proximo_bloco.hash:
                return False
            
        return True

def main():
    minha_blockchain = Blockchain()

    while True:
        print("\nAdicionar um novo bloco")
        
        item = input("Digite o nome do item: ")
        valor = input("Digite o valor do item: ")
        comprador = input("Digite o nome do comprador: ")
        vendedor = input("Digite o nome do vendedor: ")
        
        dados = {
            "Item": item,
            "Valor": valor,
            "Comprador": comprador,
            "Vendedor": vendedor
        }

        minha_blockchain.add_bloco(dados)

        if minha_blockchain.Validar():
            print("A blockchain é válida.")
        else:
            print("A blockchain não é válida!")

        continuar = input("Deseja adicionar outro bloco? (sim ou nao): ")
        if continuar.lower() != 'sim':
            break

    mostrar_blockchain(minha_blockchain.chain)

def mostrar_blockchain(chain):
    for bloco in chain:
        print(f"Bloco: {bloco.index}")
        print(f"Data e Hora: {bloco.data_e_hora}")
        print(f"Dados: {bloco.dados}")
        print(f"Hash: {bloco.hash}")
        print(f"Hash do bloco anterior: {bloco.meu_hash if bloco.index > 0 else 'N/A'}")
        print(25 * "-----")

if __name__ == "__main__":
    main()
