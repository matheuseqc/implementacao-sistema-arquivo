class Bloco:
    def __init__(self, caractere=None, ponteiro=-1):
        self.caractere = caractere  # Um caractere que representa uma parte do arquivo.
        self.ponteiro = ponteiro    # Índice do próximo bloco ou -1 se for o último.

class SistemaArquivos:
    def __init__(self, tamanho_memoria=32):
        self.tamanho_memoria = tamanho_memoria
        self.memoria = [Bloco() for _ in range(tamanho_memoria)]  # Vetor de blocos.
        self.tabela_arquivos = {}  # Armazena nome, tamanho e endereço inicial do arquivo.
        self.espacos_livres = list(range(tamanho_memoria))  # Gerenciamento de blocos livres.

    def criar_arquivo(self, nome, conteudo):
        if nome in self.tabela_arquivos:
            print(f"Arquivo '{nome}' já existe.")
            return
        
        tamanho_conteudo = len(conteudo)

        if len(self.espacos_livres) < tamanho_conteudo:
            print("Memória insuficiente para armazenar o arquivo.")
            return

        # Aloca os blocos na memória.
        endereco_inicial = self.espacos_livres.pop(0)
        endereco_atual = endereco_inicial

        for i in range(tamanho_conteudo):
            proximo_bloco = self.espacos_livres.pop(0) if i < tamanho_conteudo - 1 else -1
            self.memoria[endereco_atual] = Bloco(conteudo[i], proximo_bloco)
            endereco_atual = proximo_bloco

        # Registra o arquivo na tabela.
        self.tabela_arquivos[nome] = {"tamanho": tamanho_conteudo, "endereco": endereco_inicial}
        print(f"Arquivo '{nome}' criado com sucesso.")
        self.imprimir_memoria()

    def ler_arquivo(self, nome):
        if nome not in self.tabela_arquivos:
            print(f"Arquivo '{nome}' não encontrado.")
            return

        endereco_atual = self.tabela_arquivos[nome]["endereco"]
        conteudo = []
        
        # Percorre os blocos encadeados e reconstrói o conteúdo.
        while endereco_atual != -1:
            bloco = self.memoria[endereco_atual]
            conteudo.append(bloco.caractere)
            endereco_atual = bloco.ponteiro

        print(f"Conteúdo do arquivo '{nome}': {''.join(conteudo)}")

    def excluir_arquivo(self, nome):
        if nome not in self.tabela_arquivos:
            print(f"Arquivo '{nome}' não encontrado.")
            return

        # Libera os blocos ocupados pelo arquivo.
        endereco_atual = self.tabela_arquivos[nome]["endereco"]
        while endereco_atual != -1:
            bloco = self.memoria[endereco_atual]
            proximo = bloco.ponteiro
            self.memoria[endereco_atual] = Bloco()  # Reseta o bloco.
            self.espacos_livres.append(endereco_atual)
            endereco_atual = proximo

        self.espacos_livres.sort()  # Mantém a lista de espaços livres organizada.
        del self.tabela_arquivos[nome]
        print(f"Arquivo '{nome}' excluído com sucesso.")
        self.imprimir_memoria()

    def imprimir_memoria(self):
        print("Estado atual do disco:")
        for i, bloco in enumerate(self.memoria):
            if bloco.caractere:
                print(f"[{i}] Caractere: {bloco.caractere}, Ponteiro: {bloco.ponteiro}")
            else:
                print(f"[{i}] Bloco vazio")
        print("-" * 50)