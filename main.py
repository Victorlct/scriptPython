import os

def adicionar_prefixo_pasta(caminho_pasta):
    lista_arquivos = os.listdir(caminho_pasta)

    for nome_arquivo in lista_arquivos:
        caminho_atual = os.path.join(caminho_pasta, nome_arquivo)

        if os.path.isfile(caminho_atual):
            novo_nome_arquivo = "xxxx" + nome_arquivo
            novo_caminho = os.path.join(caminho_pasta, novo_nome_arquivo)
            os.rename(caminho_atual, novo_caminho)
            print(f"Arquivo renomeado: {nome_arquivo} -> {novo_nome_arquivo}")

caminho_da_sua_pasta = 'C:\\Users\\xxxxx\\Desktop\\iconesFim'
adicionar_prefixo_pasta(caminho_da_sua_pasta)
