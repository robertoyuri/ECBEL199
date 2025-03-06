linhas = ""
with open("arquivo.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

linhas += "\n nova linha....."

with open("novo_arquivo.txt", "w", encoding="utf-8") as novo_arquvio:
    novo_arquvio.writelines(linhas)

print(linhas)
