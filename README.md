# Implementação de Sistema de Arquivos

Este projeto implementa uma simulação de um sistema de arquivos básico em Python. O objetivo é demonstrar a alocação de blocos de memória, criação, leitura, exclusão e gerenciamento de arquivos de forma simplificada.

## Equipe

- **Adauto Balbino de Melo Sobrinho**  
  Matrícula: 22112371

- **Matheus de Melo Santos**  
  Matrícula: 22110824

## Funcionalidades

- **Adicionar Arquivo**: Cria um novo arquivo com um nome e conteúdo especificados.
- **Exibir Conteúdo do Arquivo**: Lê e exibe o conteúdo de um arquivo existente.
- **Remover Arquivo**: Exclui um arquivo e libera os blocos de memória que ele ocupava.
- **Ver Tabela de Arquivos**: Mostra a lista de arquivos armazenados, incluindo metadados como tamanho e endereço inicial.
- **Mostrar Status do Disco**: Exibe o estado atual dos blocos de memória, mostrando quais estão ocupados e quais estão livres.

## Estrutura do Código

- **MemoryBlock**: Classe que representa um bloco de memória, armazenando um caractere e um ponteiro para o próximo bloco.
- **FileSystem**: Classe que gerencia a simulação do sistema de arquivos, incluindo alocação de blocos, gerenciamento de arquivos e exibição do estado do disco.

## Requisitos

- Python 3.x
- Biblioteca padrão (sem dependências externas)

## Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu_usuario/file-system-simulation.git
2. Navegue até o diretório do projeto:
   ```bash
   cd implementacao-sistema-arquivo
3. Execute o script:
   ```bash
   python main.py

## Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
