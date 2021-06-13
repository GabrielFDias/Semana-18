import os
import glob

def palavra_no_arquivo(palavra, arquivo, case_sensitive):
    with open(arquivo, 'r') as f:
        if case_sensitive:
            for line in f:
                return palavra in line
        else:
            for line in f:
                return palavra.lower() in line.lower()
    return False

def todos_arquivos_txt():
    looking_for = ['**/*.txt', '**/*.csv']
    matcheds = list()
    if case_sensitive:
        for extension in looking_for:
            matcheds.append(glob.glob(extension, recursive=True))
        return matcheds

def encontrar_palavra(palavra, case_sensitive):
    encontrado_em = []
    arquivos = todos_arquivos_txt()
    for arquivo in arquivos:
        if palavra_no_arquivo(palavra, arquivo, case_sensitive):
            encontrado_em.append(arquivo)
    return encontrado_em

busca_napp1 = encontrar_palavra('napp', case_sensitive=True)
busca_napp1 = encontrar_palavra('napp', case_sensitive=False)
busca_napp2 = encontrar_palavra('NaPp', case_sensitive=True)
busca_napp2 = encontrar_palavra('NaPp', case_sensitive=False)