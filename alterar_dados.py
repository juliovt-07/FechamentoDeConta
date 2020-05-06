def alterar_dados(): #funcao a ser chamada no app principal
    import sqlite3
    import time

    connect = sqlite3.connect('DinalvaCabelereira.db')
    c = connect.cursor()

    data = str(input("data: "))
    data = "{}{}/{}{}/{}{}{}{}".format(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7])
    print(data)
    time.sleep(2)
    novo_ganho = float(input("Novo Ganho: "))
    novo_gasto = 0
    novo_bruto = 0

    c.execute("UPDATE dados SET ganho = ? WHERE dat = ?", (novo_ganho, data))
    connect.commit()
    print("Dados Alterados com Sucesso!")
    time.sleep(3)
alterar_dados()    