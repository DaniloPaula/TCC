# Codigo para padronizar arquivos CSV para o delimitador ','

import csv
import os

directory = "C:\\Users\\Danilo\\Desktop\\EPS\\TCC\\data\\AutoSegData\\"
for filename in os.listdir(directory):
    reader = csv.reader(open(directory+filename, "rU"), delimiter=';')
    writer = csv.writer(open(directory+"1"+filename, 'w'), delimiter=',')
    writer.writerows(reader)
