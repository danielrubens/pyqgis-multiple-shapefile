# Carregando bibliotecas no Python
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
import processing
import sys

BRAZIL = "C:\Users\daniel.rubens\Desktop\project\BR.shp"
iface.addVectorLayer(BRAZIL, "BRAZIL", "ogr")

#Convertendo sistema de coordenadas
GEO_SIRGAS = "C:\Users\daniel.rubens\Desktop\project/GEO_SIRGAS.shp"
processing.runalg("qgis:reprojectlayer", BRAZIL, "epsg:4674", GEO_SIRGAS)

# Extraindo multiplos mapas de solo com um loop
regioes =["NORTE", "NORDESTE", "SUL", "SUDESTE", "CENTRO-OESTE"]

for n in regioes:
  limite = "C:\Users\daniel.rubens\Desktop\project\lim" + n +".shp"
  processing.runalg('qgis:extractbyattribute', BRAZIL, "NM_REGIAO", 0, n, limite)
  iface.addVectorLayer(limite, "limite de " + n , "ogr")

