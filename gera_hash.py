import hashlib

def gerar_hash(nome_arquivo):
    with open(nome_arquivo, 'rb') as f:
        conteudo = f.read()
        return hashlib.sha256(conteudo).hexdigest()

# Lista de arquivos a serem verificados
arquivos = ['lei1891.txt', 'script_dados.txt']

# Calcula e exibe o hash de cada arquivo
for arq in arquivos:
    hash_valor = gerar_hash(arq)
    print(f"Hash de {arq}: {hash_valor}")
