"""

### Ordenar os usuários pelo percentual de espaço ocupado; ###

"""

def conversor_mb(n):
    return n * 0.00000095367432


def porcentagem_mb(n, total):
    return (n / total) * 100


relatorio = {}
dados = []
somar_dados = 0
media_dados = 0
qtde = 0

with open('c:/temp/usuarios.txt', 'r') as arquivo:
    for linha in arquivo:
        cadastro = linha.strip()
        relatorio['nome'] = linha[:15].strip()
        relatorio['tamanho'] = conversor_mb(int(linha[16:].strip()))
        dados.append(relatorio.copy())

    for dado in dados:
        qtde += 1
        somar_dados += dado['tamanho']

    media_dados = somar_dados / qtde

    for dado in dados:
        dado['porcentagem'] = porcentagem_mb(dado['tamanho'], somar_dados)

# Ordenando um dicionário dentro de uma lista
dados = sorted(dados, key=lambda k: k['tamanho'], reverse=True)

dados_primeiros = int(input("Primeiros em uso. Digite quantos vão aparecer na lista: "))

# Mostrando os primeiros da lista
dados = dados[:dados_primeiros]


with open('c:/temp/relatorio_projeto.txt', 'w') as arquivo:

    arquivo.writelines(f"ACME Inc.               Uso do espaço em disco pelos usuários\n")
    arquivo.writelines(f"------------------------------------------------------------------------\n")
    arquivo.writelines(f"Nr.   Usuário        Espaço utilizado     % do uso\n")
    arquivo.writelines('\n')

    for v, dado in enumerate(dados):
        arquivo.writelines(f"{v+1:<5} {dado['nome']:<12}{dado['tamanho']:>10.2f} MB{dado['porcentagem']:>18.2f}%\n")

    arquivo.writelines('\n')
    arquivo.writelines(f'Espaço total ocupado: {somar_dados:.2f} MB\n')
    arquivo.writelines(f'Espaço médio ocupado: {media_dados:.2f} MB\n')
