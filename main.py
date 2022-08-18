from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd, time
df = pd.DataFrame
textocaminho = ''
valor = 0

def agregarProcesso():
    global valor
    valor = valor + 10
    if valor > 100:
        valor=10
    ui.progressBar.setValue(valor)
    time.sleep(1)

def caminhoExcel():
    textocaminho = QtWidgets.QFileDialog.getOpenFileName()[0]
    ui.txt_caminho_excel.setText('CARREGANDO')
    df = pd.read_excel(textocaminho)
    ui.txt_caminho_excel.setText(textocaminho)
    global valor
    valor=0
    agregarProcesso()
    ui.status_txt.setText('Arquivo carregado')
    
def executar():
    try:
        global valor
        valor=0
        bancodedados = ui.comboBox.currentText()
        user = ui.nome_user.text()
        ui.status_txt.setText('Conectando ao banco...')
        agregarProcesso()
        passw = ui.nome_passw.text()
        agregarProcesso()
        ui.status_txt.setText('Estabelecendo conexão...')
        host = ui.nome_host.text()
        agregarProcesso()
        ui.status_txt.setText('Conectado...')
        nomedabd = ui.nome_banco.text()
        agregarProcesso()
        ui.status_txt.setText('Carregando tabelas...')
        tabela = ui.nome_tabela.text()
        agregarProcesso()
        ui.status_txt.setText('Transferindo tabelas...')
        from sqlalchemy import create_engine
        # format: mysql://user:pass@host/db
        agregarProcesso()
        ui.status_txt.setText('Criando código sql...')
        query = bancodedados + '://' + user + ':' + passw + '@' + host + '/' + nomedabd
        agregarProcesso()
        ui.status_txt.setText('Inserindo ao banco...')
        engine = create_engine(query)
        agregarProcesso()
        print(engine)
        ui.status_txt.setText('Completo')
        print(tabela)
        df.to_sql(tabela, con=engine)
        agregarProcesso()
        ui.status_txt.setText('Sucesso')
    except Exception as err:
        cd_error = err
        ui.status_txt.setText('Erro: '+ str(cd_error) + '\n Tente novamente')


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(418, 563)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 134, 401, 121))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.l_conect = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.l_conect.setContentsMargins(0, 0, 0, 0)
        self.l_conect.setObjectName("l_conect")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.l_conect.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.nome_host = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.nome_host.setObjectName("nome_host")
        self.l_conect.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.nome_host)
        self.line_3 = QtWidgets.QFrame(self.formLayoutWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.l_conect.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.line_3)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.l_conect.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.nome_tabela = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.nome_tabela.setObjectName("nome_tabela")
        self.l_conect.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.nome_tabela)
        self.line_2 = QtWidgets.QFrame(self.formLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.l_conect.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.line_2)
        self.line_4 = QtWidgets.QFrame(self.formLayoutWidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_4.setObjectName("line_4")
        self.l_conect.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.line_4)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.l_conect.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 380, 401, 101))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.l_button = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.l_button.setContentsMargins(0, 0, 0, 0)
        self.l_button.setObjectName("l_button")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        
        self.l_button.addWidget(self.pushButton)
        self.txt_caminho_excel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.txt_caminho_excel.setText("")
        self.txt_caminho_excel.setObjectName("txt_caminho_excel")
        self.l_button.addWidget(self.txt_caminho_excel)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.l_button.addWidget(self.pushButton_2)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 490, 401, 61))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.l_progresso = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.l_progresso.setContentsMargins(0, 0, 0, 0)
        self.l_progresso.setObjectName("l_progresso")
        self.status_txt = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.status_txt.setText("")
        self.status_txt.setObjectName("status_txt")
        self.l_progresso.addWidget(self.status_txt)
        self.progressBar = QtWidgets.QProgressBar(self.verticalLayoutWidget_3)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.l_progresso.addWidget(self.progressBar)
        self.formLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 0, 401, 131))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.line_14 = QtWidgets.QFrame(self.formLayoutWidget_2)
        self.line_14.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_14.setObjectName("line_14")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.line_14)
        self.line_15 = QtWidgets.QFrame(self.formLayoutWidget_2)
        self.line_15.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_15.setObjectName("line_15")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.line_15)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_10)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_6)
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.comboBox.setObjectName("comboBox")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.comboBox)
        self.comboBox.addItems(["postgresql", "mysql", "mssql", "sqlite", "oracle"])
        self.line_5 = QtWidgets.QFrame(self.formLayoutWidget_2)
        self.line_5.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_5.setObjectName("line_5")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.line_5)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_7)
        self.nome_banco = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.nome_banco.setObjectName("nome_banco")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.nome_banco)
        self.line_9 = QtWidgets.QFrame(self.formLayoutWidget_2)
        self.line_9.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_9.setObjectName("line_9")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.line_9)
        self.formLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(10, 254, 401, 121))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.l_conect_2 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.l_conect_2.setContentsMargins(0, 0, 0, 0)
        self.l_conect_2.setObjectName("l_conect_2")
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.l_conect_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_11)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_4.setObjectName("label_4")
        self.l_conect_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_5.setObjectName("label_5")
        self.l_conect_2.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        self.nome_user = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.nome_user.setObjectName("nome_user")
        self.l_conect_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.nome_user)
        self.nome_passw = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.nome_passw.setObjectName("nome_passw")
        self.l_conect_2.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.nome_passw)
        self.line_12 = QtWidgets.QFrame(self.formLayoutWidget_3)
        self.line_12.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_12.setObjectName("line_12")
        self.l_conect_2.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.line_12)
        self.line_13 = QtWidgets.QFrame(self.formLayoutWidget_3)
        self.line_13.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_13.setObjectName("line_13")
        self.l_conect_2.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.line_13)
        self.pushButton.clicked.connect(caminhoExcel)
        self.pushButton_2.clicked.connect(executar)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Excel para Banco de dados"))
        self.label_2.setText(_translate("Form", "Host:"))
        self.label_3.setText(_translate("Form", "Nome da tabela:"))
        self.label.setText(_translate("Form", "Conexão"))
        self.pushButton.setText(_translate("Form", "Selecione o arquivo Excel"))
        self.pushButton_2.setText(_translate("Form", "Iniciar"))
        self.label_10.setText(_translate("Form", "Banco de dados"))
        self.label_6.setText(_translate("Form", "Linguagem:"))
        self.label_7.setText(_translate("Form", "Nome:"))
        self.label_11.setText(_translate("Form", "Login"))
        self.label_4.setText(_translate("Form", "Usúario:"))
        self.label_5.setText(_translate("Form", "Senha:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())

