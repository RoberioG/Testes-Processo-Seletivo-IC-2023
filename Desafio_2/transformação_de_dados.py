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
    listaTabelas = tabula.read_pdf("AnexoI-Listacompletadeprocedimentos.pdf", encoding='cp1252', lattice=True, pages=list(range(3, 181)))
    manipulaTabelas(listaTabelas)
    zipTabela()

main()