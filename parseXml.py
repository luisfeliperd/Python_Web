
###Script para extrair dados de XML (Parse).###
#Feito por LuisMDlab e eduardo2s# - 23/03/2018

from urllib.request import urlopen #Importa Urlopen para abrir o link do XML.
from xml.dom.minidom import parse #Importa o parser do XML.

#Pegar um Atributo de uma Tag dentro do XML.
xmldoc = parse(urlopen('LinkouURL')) #Abrir o Link do XML.
link_xml = xmldoc.getElementsByTagName('NomedaTag') #Selecionar uma Tag do XML.
print(link_xml[1].attributes['NomedoAtributo'].value) #Selecionar um atributo dessa Tag.
