import openpyxl
#função que cria a planilha (é necessária a importação do openpyxl para isso)
def CriarPlanilha():
    book= openpyxl.Workbook()
    book.create_sheet('SeusDados')
    page=book["SeusDados"]
    page.append(['Nome','Sobrenome','Idade','Nacionalidade'])
    page.append([nome,sobrenome,idade,nacionalidade])
    book.save('.\Desktop\Dados.xlsx')

#função que cria o arquivo de texto
def CriarArquivo():
    with open (".\Desktop\Dados.txt","w") as f:
        f.write("Olá, {} :)\n".format(nome_completo))
        f.write("Esses são seus dados: \n")
        f.write("Nome: {}\n".format(nome))
        f.write("Sobrenome: {}\n".format(sobrenome))
        f.write("Idade: {}\n".format(idade))
        f.write("Nacionalidade: {}\n".format(nacionalidade))
        f.close()     

#Pede os dados do usuário
nome=str(input("Digite seu primeiro nome: "))
sobrenome=str(input("Digite seu sobrenome: "))
idade=int(input("Qual sua idade? "))
nacionalidade=str(input("Qual sua nacionalidade? "))
nome_completo=nome+" "+sobrenome

#chama as funções
CriarArquivo()
CriarPlanilha()