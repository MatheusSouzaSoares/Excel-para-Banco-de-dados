import pandas as pd
from tkinter import *
from tkinter.ttk import Combobox
from getpass import getpass
textocaminho =''
bancodedados =''
user=''
passw=''
host=''
nomedabd=''
tabela=''


def caminhoExcel():
    from tkinter import filedialog as dlg
    path = dlg.askopenfile().name
    textocaminho = path
    print(textocaminho)
    texto_excel = Label(janela, text=textocaminho)
    texto_excel.grid(column=0, row=2)
    return path


def executar():
    bancodedados = selecionar_bd.get()
    user = selecionar_user.get()
    passw = selecionar_pass.get()
    host = selecionar_host.get()
    nomedabd = namebd.get()
    tabela = tabela_namt.get()
    df = pd.read_excel(textocaminho)
    from sqlalchemy import create_engine
    # format: mysql://user:pass@host/db
    #engine = create_engine(bd'://'user':'senha'@'host'/'database)
    #df.to_sql(tabela, con=engine)
    print(bancodedados+'://'+user+':'+passw+'@'+host+'/'+nomedabd+tabela)


janela = Tk()
janela.title('Excel para Banco de Dados')
janela.geometry('350x500')

botao_excel = Button(janela, text='Selecione o arquivo XlSX', command=caminhoExcel)
botao_excel.grid(column=0, row=1)

texto_selecionar_host = Label(text='Host:', justify='left')
texto_selecionar_host.grid(column=0, row=3)

selecionar_host = Text(height=1, width=40)
selecionar_host.grid(column=0, row=4)

texto_selecionar_bd = Label(text='Banco de dados:', justify='left')
texto_selecionar_bd.grid(column=0, row=5)

selecionar_bd = Combobox(janela, values=["postgresql", "mysql", "mssql", "sqlite", "oracle" ])
selecionar_bd.grid(column=0, row=6, padx=1, pady=10)

texto_selecionar_namebd = Label(text='Data Base:', justify='left')
texto_selecionar_namebd.grid(column=0, row=7)

namebd = Text(height=1, width=40)
namebd.grid(column=0, row=8, padx=1, pady=5)

texto_selecionar_user = Label(text='Usuário:', justify='left')
texto_selecionar_user.grid(column=0, row=9)

selecionar_user = Text(height=1, width=40)
selecionar_user.grid(column=0, row=10, padx=1, pady=5)

texto_selecionar_pass = Label(text='Senha:', justify='left')
texto_selecionar_pass.grid(column=0, row=11)

selecionar_pass = Entry(janela, show="*")
selecionar_pass.grid(column=0, row=12)

tabela_name = Label(text='Nome da tabela: ', justify='left')
tabela_name.grid(column=0, row=13)

tabela_namt = Text(height=1, width=40)
tabela_namt.grid(column=0, row=14, padx=1, pady=5)

botao_excel = Button(janela, text='Confirmar', command=executar)
botao_excel.grid(column=0, row=15)

janela.mainloop()
