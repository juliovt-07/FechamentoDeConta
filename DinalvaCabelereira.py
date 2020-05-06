import sqlite3
import time
import datetime 

connection = sqlite3.connect("DinalvaCabelereira.db")
c = connection.cursor()

dat = time.strftime("%d/%m/%Y")
go = 0
gt = 0
br = 0
GanhoTotal = 0
def create_table():    
    c.execute("CREATE TABLE IF NOT EXISTS dados (dat text, ganho real, gasto  real, bruto real)")
create_table()

def inserir():
    c.execute("INSERT INTO dados (dat, ganho, gasto, bruto) VALUES(?,?,?,?)",(dat, go, gt, br))
    
    connection.commit()
print("==================Dinalva Cabelereira=======================")
time.sleep(1)
print("===================Fechamento Diario========================")
time.sleep(1)    
dat = time.strftime("%d/%m/%Y")
escolha = 1
cont = 0
v = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
while escolha == 1:
  
  print("[codigo] nome")
  print("[ 10 ] Produto 1")
  print("[ 11 ] Produto 2")
  print("[ 12 ] Produto 3")
  print("[ 13 ] Produto 4")
  print("[ 14 ] Produto 5")
  print("[ 15 ] Produto 6")
  codigo = int(input("Codigo: "))
  if codigo <= 0:
    print("codigo invalido!")
  elif codigo == 10:
    valorEmpresa = 91
    valorSalao = valorEmpresa+(valorEmpresa*0.40)
    print("Valor (empresa): {} R$".format(valorEmpresa))
    print("Valor da venda: {} R$".format(valorSalao))
    #print("Dizimo: {}".format((valorSalao-valorEmpresa)*0.10))
    print("Ganho: {} R$".format(valorSalao-valorEmpresa))
  elif codigo == 11:
    valorEmpresa = 24
    valorSalao = valorEmpresa+(valorEmpresa*0.40)
    print("Valor (empresa): {} R$".format(valorEmpresa))
    print("Valor da venda: {} R$".format(valorSalao))
    #print("Dizimo: {}".format((valorSalao-valorEmpresa)*0.10))
    print("Ganho: {} R$".format(valorSalao-valorEmpresa))
  elif codigo == 12:
    valorEmpresa = 130
    valorSalao = valorEmpresa+(valorEmpresa*0.40)
    print("Valor (empresa): {} R$".format(valorEmpresa))
    print("Valor da venda: {} R$".format(valorSalao))
    #print("Dizimo: {}".format((valorSalao-valorEmpresa)*0.10))
    print("Ganho: {} R$".format(valorSalao-valorEmpresa))
  elif codigo == 13:
    valorEmpresa = 65
    valorSalao = valorEmpresa+(valorEmpresa*0.40)
    print("Valor (empresa): {} R$".format(valorEmpresa))
    print("Valor da venda: {} R$".format(valorSalao))
    #print("Dizimo: {}".format((valorSalao-valorEmpresa)*0.10))
    print("Ganho: {} R$".format(valorSalao-valorEmpresa))
  elif codigo == 14:
    valorEmpresa = 48.50
    valorSalao = valorEmpresa+(valorEmpresa*0.40)
    print("Valor (empresa): {} R$".format(valorEmpresa))
    print("Valor da venda: {} R$".format(valorSalao))
    #print("Dizimo: {}".format((valorSalao-valorEmpresa)*0.10))
    print("Ganho: {} R$".format(valorSalao-valorEmpresa))
  elif codigo == 15:
    valorEmpresa = 80.50
    valorSalao = valorEmpresa+(valorEmpresa*0.40)
    print("Valor (empresa): {} R$".format(valorEmpresa))
    print("Valor da venda: {} R$".format(valorSalao))
    #print("Dizimo: {}".format((valorSalao-valorEmpresa)*0.10))
    print("Ganho: {} R$".format(valorSalao-valorEmpresa))
    
  time.sleep(1)
  print("|"*35) 
  v[cont] = valorSalao-valorEmpresa
  #print(cont)
  #print(v[:(cont+1)])
  cont = cont+1
  time.sleep(1)
  escolha = int(input("[Codigo]\n[ 1 ] Adicionar Produto\n[ 2 ] Mostrar Valor Total\n- "))
GanhoTotal = v[0]+v[1]+v[2]+v[3]+v[4]+v[5]+v[6]+v[7]+v[8]+v[9]+v[10]+v[11]+v[12]  
print("Ganho Total: {} R$".format(GanhoTotal))
go = GanhoTotal
#gt = float(input("=======================Gastos: ========================\n"))
#br = float(input("=======================Bruto: =========================\n"))
gt = 0
br = 0
print("=================Armazenado com sucesso======================")
time.sleep(3)
inserir()