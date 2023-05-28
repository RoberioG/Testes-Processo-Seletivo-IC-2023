import requests
from bs4 import BeautifulSoup
import os
import zipfile

def zipAnexos():
    z = zipfile.ZipFile('anexos.zip', 'w')

    for folder, subfolders, files in os.walk('./anexos'):
        for file in files:
            if file.endswith('.pdf') or file.endswith('.xlsx'):
                z.write(os.path.join(folder, file), file, compress_type = zipfile.ZIP_DEFLATED)

    z.close()


def downloadAnexos(anexos):

    os.makedirs('./anexos')

    for x in anexos:
        file = requests.get(x['link'])

        arquivo = open(f"anexos/{x['nome']}", 'wb')
        arquivo.write(file.content)
        arquivo.close()


def getAnexos(url):
    site = requests.get(url)
    soup = BeautifulSoup(site.content, 'html.parser')

    links = []

    for anexo in soup.find_all(class_="callout"): 
        dic_anexos = {'nome' : '', 'link' : ''}
        if "Anexo" in anexo.getText():
            dic_anexos['nome'] = str(anexo.get_text().replace(" ", "").replace("(", "").replace(")", ""))
            dic_anexos['link'] = anexo.find('a').get('href')
            links.append(dic_anexos)

    return links


def main():

    urlPaginaPrincipal = "https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude"

    anexos = getAnexos(urlPaginaPrincipal)
    downloadAnexos(anexos)
    zipAnexos()


main()