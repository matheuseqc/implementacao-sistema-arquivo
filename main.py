import os
import time

class MemoryBlock:
    def __init__(self, char, pointer=None):
        self.char = char  # Um caractere do arquivo
        self.pointer = pointer  # Ponteiro para o próximo bloco (None se for o último bloco)

class FileSystem:
    def __init__(self, total_blocks):
        self.total_blocks = total_blocks
        self.disk = [None] * total_blocks  # Disco simulado com blocos vazios
        self.file_table = {}  # Armazena metadados dos arquivos (nome, tamanho, endereço inicial)
        self.free_blocks = list(range(total_blocks))  # Lista de blocos livres

    def allocateBlocks(self, size):
        if len(self.free_blocks) < size:
            print("Memória insuficiente.")
            return None
        # Aloca os blocos necessários
        allocated = [self.free_blocks.pop(0) for _ in range(size)]
        return allocated

    def freeBlock(self, block_index):
        # Insere o bloco liberado de volta na lista de blocos livres, mantendo a ordem
        self.free_blocks.append(block_index)
        self.free_blocks.sort()  # Ordena para reutilizar blocos liberados em ordem crescente

    def createFile(self):
        name = input("Digite o nome do arquivo: ")
        content = input("Digite o conteúdo do arquivo: ")
        if name in self.file_table:
            print(f"Arquivo '{name}' já existe.")
            return
        size = len(content)
        blocks_needed = size
        allocated_blocks = self.allocateBlocks(blocks_needed)
        if not allocated_blocks:
            return

        # Vincula os blocos e armazena o conteúdo
        for i, char in enumerate(content):
            next_block = allocated_blocks[i + 1] if i + 1 < size else None
            self.disk[allocated_blocks[i]] = MemoryBlock(char, next_block)

        # Adiciona metadados do arquivo
        self.file_table[name] = {
            'size': size,
            'start': allocated_blocks[0]
        }
        print(f"Arquivo '{name}' criado com sucesso.")

    def readFile(self):
        name = input("Digite o nome do arquivo a ser lido: ")
        if name not in self.file_table:
            print(f"Arquivo '{name}' não existe.")
            return
        start = self.file_table[name]['start']
        content = []
        current = start
        while current is not None:
            block = self.disk[current]
            content.append(block.char)
            current = block.pointer
        print(f"Conteúdo do arquivo '{name}':", ''.join(content))

    def deleteFile(self):
        name = input("Digite o nome do arquivo a ser excluído: ")
        if name not in self.file_table:
            print(f"Arquivo '{name}' não existe.")
            return

        # Libera os blocos alocados
        start = self.file_table[name]['start']
        current = start
        while current is not None:
            block = self.disk[current]
            next_block = block.pointer
            self.disk[current] = None
            self.freeBlock(current)  # Usa o método para liberar blocos de forma ordenada
            current = next_block

        # Remove metadados do arquivo
        del self.file_table[name]
        print(f"Arquivo '{name}' excluído com sucesso.")

    def printDisk(self):
        print("\nEstado do Disco:")
        print("-" * 50)
        for i, block in enumerate(self.disk):
            if block:
                print(f"[{i}] Char: '{block.char}', Pointer: {block.pointer}")
            else:
                print(f"[{i}] Vazio")
        print("-" * 50)

    def printFileTable(self):
        print("\nTabela de Arquivos:")
        print("-" * 50)
        if not self.file_table:
            print("Nenhum arquivo armazenado.")
        else:
            print(f"{'Nome':<15}{'Tamanho':<10}{'Endereço':<10}")
            for name, data in self.file_table.items():
                print(f"{name:<15}{data['size']:<10}{data['start']:<10}")
        print("-" * 50)

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    sistema_arquivos = FileSystem(total_blocks=32)
    
    while True:
        clearScreen()
        print("=" * 50)
        print("Bem-vindo à Simulação de Sistema de Arquivos".center(50))
        print("=" * 50)
        print("[1] Adicionar Arquivo")
        print("[2] Exibir Conteúdo do Arquivo")
        print("[3] Remover Arquivo")
        print("[4] Ver Tabela de Arquivos")
        print("[5] Mostrar Status do Disco")
        print("[0] Sair do Programa\n")
        
        escolha_usuario = input("Selecione uma opção: ")

        if escolha_usuario == '1':
            sistema_arquivos.createFile()
            input("\nPressione Enter para prosseguir...")
        elif escolha_usuario == '2':
            sistema_arquivos.readFile()
            input("\nPressione Enter para prosseguir...")
        elif escolha_usuario == '3':
            sistema_arquivos.deleteFile()
            input("\nPressione Enter para prosseguir...")
        elif escolha_usuario == '4':
            sistema_arquivos.printFileTable()
            input("\nPressione Enter para prosseguir...")
        elif escolha_usuario == '5':
            sistema_arquivos.printDisk()
            input("\nPressione Enter para prosseguir...")
        elif escolha_usuario == '0':
            print("\nSaindo do programa...")
            time.sleep(3)
            break
        else:
            print("\nEscolha inválida! Por favor, tente novamente.")
            time.sleep(3)

if __name__ == "__main__":
    main()
