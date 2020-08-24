# Codigo para converter tabelas Access para CSV

import csv
import pyodbc

directory = str(input("Digite o diretorio: "))
file_name = str(input("Digite o nome do arquivo Access: "))
table = str(input("Digite o nome da table contida no arquivo Access: "))

# set up some constants
MDB = directory+"\\"+file_name
DRV = '{Microsoft Access Driver (*.mdb, *.accdb)}'

# connect to db
con = pyodbc.connect('DRIVER={};DBQ={}'.format(DRV, MDB))
cur = con.cursor()

# run a query and get the results
SQL = 'SELECT * FROM '+table+';'  # your query goes here
rows = cur.execute(SQL).fetchall()

# you could change the mode from 'w' to 'a' (append) for any subsequent queries
with open(directory+'\\'+table+'.csv', 'w') as fou:
    csv_writer = csv.writer(fou, delimiter=",", quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow([i[0] for i in cur.description])
    csv_writer.writerows(rows)

cur.close()
con.close()