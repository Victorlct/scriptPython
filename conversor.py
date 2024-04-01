from PIL import Image
import os
import svgwrite

def converter_imagem(caminho_pasta, formato_destino):
    lista_arquivos = os.listdir(caminho_pasta)

    for nome_arquivo in lista_arquivos:
        caminho_atual = os.path.join(caminho_pasta, nome_arquivo)

        if os.path.isfile(caminho_atual) and nome_arquivo.lower().endswith(".ico"):
            imagem = Image.open(caminho_atual)

            if formato_destino == "ico":
                novo_nome_arquivo = os.path.splitext(nome_arquivo)[0] + ".ico"
                novo_caminho = os.path.join(caminho_pasta, novo_nome_arquivo)
                imagem.save(novo_caminho, format=formato_destino.upper())
            elif formato_destino == "svg":
                novo_nome_arquivo = os.path.splitext(nome_arquivo)[0] + ".svg"
                novo_caminho = os.path.join(caminho_pasta, novo_nome_arquivo)
                dwg = svgwrite.Drawing(novo_caminho, profile='tiny')
                dwg.add(dwg.image(href=caminho_atual, size=(imagem.width, imagem.height)))
                dwg.save()
            else:
                print("Formato de destino não suportado.")
                return

            print(f"Arquivo convertido: {nome_arquivo} -> {novo_nome_arquivo}")

caminho_da_sua_pasta = 'C:\\Users\\xxxx\\Desktop\\iconesEdpSvg'
formato_destino = "svg" 
converter_imagem(caminho_da_sua_pasta, formato_destino)
