import tabula
import pandas
import zipfile

def manipulaTabelas(listaTabelas):

    tabelaPrincipal = listaTabelas[0]
    del listaTabelas[0]

    for tabela in listaTabelas:
        tabelaPrincipal = pandas.concat([tabelaPrincipal, tabela], ignore_index=True)

    tabelaPrincipal.drop(tabelaPrincipal.columns[13:], axis=1, inplace=True)
    tabelaPrincipal = tabelaPrincipal.set_index("PROCEDIMENTO")
    tabelaPrincipal = tabelaPrincipal.rename(columns={"OD": "SEG. ODONTOLÓGICO", "AMB": "SEG. AMBULATÓRIO"})

    return tabelaPrincipal.to_csv('AnexoI-Listacompletadeprocedimentos.csv')


def zipTabela():
    tabelaZip = zipfile.ZipFile('Teste_Roberio_Girao.zip', 'w', zipfile.ZIP_DEFLATED)
    tabelaZip.write('AnexoI-Listacompletadeprocedimentos.csv')
    tabelaZip.close()


def main():
    listaTabelas = tabula.read_pdf("AnexoI-Listacompletadeprocedimentos.pdf", encoding='cp1252', pages=list(range(3, 181)))
    manipulaTabelas(listaTabelas)
    zipTabela()

main()



"""
print(len(listaTabelas))


print(">>> TABELA PRINCIPAL <<<")
display(tabelaPrincipal)

##print(">>> LISTA DE TABELAS <<<")
##display(listaTabelas)




## até aqui beleza



#tabelaPrincipal.columns = tabelaPrincipal.iloc[0]
#tabelaPrincipal = tabelaPrincipal[1:]


print(">>> TABELA PRINCIPAL <<<")
display(tabelaPrincipal)

print(">>> LISTA DE TABELAS <<<")
display(listaTabelas)
"""


'''
tabela = listaTabelas[0]
tabela.columns = tabela.iloc[0]
tabela[[0,1]] = tabela["Variação percentual"].str.split(" ", expand=True)
tabela = tabela[1:9]

tabela = tabela.set_index("R$ milhões")
tabela.columns = tabela.iloc[0]
tabela = tabela[1:]
tabela = tabela.drop("1T21/4T20 1T21/1T20", axis=1) #exclui de acordo com o eixo, uma linha (0) ou coluna (1)
display(tabela)
'''

