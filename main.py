import pandas as pd
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QLineEdit,QComboBox
textocaminho = ''

def caminhoExcel():
    textocaminho =QtWidgets.QFileDialog.getOpenFileName()[0]
    janela.txt_caminho_excel.setText('CARREGANDO')
    df = pd.read_excel(textocaminho)
    janela.txt_caminho_excel.setText(textocaminho)

def executar():
    bancodedados = janela.nome_banco_de_dados.currentText()
    print(bancodedados)
    user = janela.nome_user.text()
    print(user)
    passw = janela.nome_senha.text()
    print(passw)
    host = janela.nome_host.text()
    print(host)
    nomedabd = janela.nome_db.text()
    print(nomedabd)
    tabela = janela.nome_tabela.text()
    print(tabela)
    print('Sucesso')
    from sqlalchemy import create_engine
    # format: mysql://user:pass@host/db
    print('Sucesso')
    query = bancodedados +'://' + user + ':' + passw+ '@' + host+ '/' + nomedabd
    print('Sucesso')
    engine = create_engine(query)
    print(engine)
    df.to_sql('tabela', con=engine)
    print('sucesso')


app = QtWidgets.QApplication([])
janela = uic.loadUi("tela_excel_para_banco_de_dados.ui")
janela.pushButton.clicked.connect(caminhoExcel)
janela.pushButton_2.clicked.connect(executar)

janela.nome_banco_de_dados = QComboBox(janela)
janela.nome_banco_de_dados.move(130,130)
janela.nome_banco_de_dados.resize(351,31)
janela.nome_banco_de_dados.addItems(["postgresql", "mysql", "mssql", "sqlite", "oracle" ])

janela.nome_db = QLineEdit(janela)
janela.nome_db.move(130,170)
janela.nome_db.resize(351,31)

janela.nome_user = QLineEdit(janela)
janela.nome_user.move(130,250)
janela.nome_user.resize(351,31)

janela.nome_senha = QLineEdit(janela)
janela.nome_senha.move(130,290)
janela.nome_senha.resize(351,31)

janela.nome_host = QLineEdit(janela)
janela.nome_host.move(130,210)
janela.nome_host.resize(351,31)

janela.nome_tabela = QLineEdit(janela)
janela.nome_tabela.move(130,330)
janela.nome_tabela.resize(351,31)

janela.show()
app.exec()
