import pandas as pd
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QLineEdit

textocaminho = ''
bancodedados = ''
user = ''
passw = ''
host = ''
nomedabd = ''
tabela = ''


def caminhoExcel():
    textocaminho = QtWidgets.QFileDialog.getOpenFileName()[0]
    print(textocaminho)
    janela.txt_caminho_excel.setText(textocaminho)


def executar():
    bancodedados = janela.nome_banco_de_dados.currentText()
    user = janela.janela.nome_user.currentText()
    passw = janela.nome_senha.currentText()
    host = janela.nome_host.currentText()
    nomedabd = janela.nome_db.currentText()
    tabela = janela.nome_tabela.currentText()
    df = pd.read_excel(textocaminho)
    from sqlalchemy import create_engine
    # format: mysql://user:pass@host/db
    # engine = create_engine(bd'://'user':'senha'@'host'/'database)
    # df.to_sql(tabela, con=engine)
    print(bancodedados + '://' + user + ':' + passw + '@' + host + '/' + nomedabd + tabela)


app = QtWidgets.QApplication([])
janela = uic.loadUi("tela_excel_para_banco_de_dados.ui")
janela.pushButton.clicked.connect(caminhoExcel)
janela.nome_banco_de_dados.addItems(["postgresql", "mysql", "mssql", "sqlite", "oracle" ])
janela.pushButton_2.clicked.connect(executar)
janela.show()
app.exec()
