import gerenciaArquivos 

sistema = gerenciaArquivos.SistemaArquivos()


sistema.criar_arquivo("f01.file", "PERNAMBUCO")
sistema.criar_arquivo("f02.file", "ALAGOAS")


sistema.ler_arquivo("f01.file")
sistema.ler_arquivo("f02.file")


sistema.excluir_arquivo("f01.file")


sistema.ler_arquivo("f01.file")


sistema.criar_arquivo("f03.file", "SANTACATARINA")