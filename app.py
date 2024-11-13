import os
import shutil
import subprocess

# Função para abrir o CMD
def abrir_cmd():
    subprocess.run("start cmd", shell=True)  # Abre o CMD

# Função para limpar uma pasta específica
def limpar_pasta(pasta):
    for arquivo in os.listdir(pasta):
        caminho_arquivo = os.path.join(pasta, arquivo)
        try:
            if os.path.isfile(caminho_arquivo) or os.path.islink(caminho_arquivo):
                os.unlink(caminho_arquivo)  # Exclui arquivo ou link
            elif os.path.isdir(caminho_arquivo):
                shutil.rmtree(caminho_arquivo)  # Exclui diretório
        except Exception as e:
            print(f"Erro ao excluir {caminho_arquivo}: {e}")

# Abrir o CMD
abrir_cmd()

# Definindo as pastas TEMP e %TEMP%
temp_folder = os.getenv("TEMP")           # Caminho para a pasta %TEMP%
local_temp_folder = os.path.join(os.getenv("LOCALAPPDATA"), "Temp")  # Caminho para a pasta TEMP

# Limpar ambas as pastas
print("Limpando a pasta %TEMP%...")
limpar_pasta(temp_folder)

print("Limpando a pasta TEMP...")
limpar_pasta(local_temp_folder)

print("Limpeza concluída com sucesso!")
