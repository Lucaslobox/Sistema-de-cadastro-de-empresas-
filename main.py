from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox, QTableWidgetItem)
from PySide6.QtCore import QFile, QTextStream
from ui_main import Ui_MainWindow
from PySide6 import QtCore
import sys
import pandas as pd
import sqlite3
from database import Data_base
from api_functions import consulta_cnpj



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("BlackWolf - Sistema de cadastro de empresas")

        
########### Importando theme ##################
        app = QApplication.instance()
        qss_file_path = "C:/Users/Lucas Lobo/Desktop/projetos/cadastro_empresas/theme.qss"
        qss_file = QFile(qss_file_path)
        qss_file.open(QFile.ReadOnly | QFile.Text)
        stream = QTextStream(qss_file)
        qss = stream.readAll()

        app.setStyleSheet(qss)



############################# Sistema de botões - páginas ########################################

        self.ui.btn_home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pg_home))
        self.ui.btn_cadastro.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_cadastro))
        self.ui.btn_Contatos.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pg_contatos))


        self.ui.btn_toggle.clicked.connect(self.container_menu)
        

#########################  PREENCHER AUTOMATICAMENTE OS DADOS DO CNPJ ###############################


        self.ui.txt_cnpj.editingFinished.connect(self.consult_api)
        
######################################## Sistema de botões - tabela #################################

        self.ui.btn_cadastrar.clicked.connect(self.cadastrar_empresas)
        self.ui.btn_alterar.clicked.connect(self.updata_company)
        self.ui.btn_excluir.clicked.connect(self.deletar_empresa)
        self.ui.btn_gerarexecel.clicked.connect(self.gerar_excel_2)

        self.buscar_empresas()

###############################  Animação do Menu lateral #############################################   

    def container_menu(self):
        width = self.ui.container_menu.width()

        if width == 9:
            newWidth = 200
        else:
            newWidth = 9

        self.animation = QtCore.QPropertyAnimation(self.ui.container_menu, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

################ Função de consultar uma API e atribuição aos campos correspondentes ####################

    def consult_api(self):
        campos = consulta_cnpj(self.ui.txt_cnpj.text())

        self.ui.txt_nmempresarial.setText(campos[0])
        self.ui.txt_logradouro.setText(campos[1])
        self.ui.txt_numero.setText(campos[2])
        self.ui.txt_complemento.setText(campos[3])
        self.ui.txt_bairro.setText(campos[4])
        self.ui.txt_municipio.setText(campos[5])
        self.ui.txt_uf.setText(campos[6])
        self.ui.txt_cep.setText(campos[7].replace('.', '').replace('-',''))
        self.ui.txt_telefone.setText(campos[8].replace('(','').replace('-','').replace(')',''))
        self.ui.txt_email.setText(campos[9])


################################ cadastrar informações da empresa na base de dados ############################

    def cadastrar_empresas(self):
        db = Data_base()
        db.connect()

        fullDataSet = (
            self.ui.txt_cnpj.text(),
            self.ui.txt_nmempresarial.text(),
            self.ui.txt_logradouro.text(),
            self.ui.txt_numero.text(),
            self.ui.txt_complemento.text(),
            self.ui.txt_bairro.text(),
            self.ui.txt_municipio.text(),
            self.ui.txt_uf.text(),
            self.ui.txt_cep.text(),
            self.ui.txt_telefone.text().strip(),
            self.ui.txt_email.text()
        )


        resp = db.register_company(fullDataSet)

        if resp == "OK":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Casdastro Realizado")
            msg.setText("Cadastro Realizado com sucesso")
            msg.exec()
            db.close_connection()
            return
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Erro")
            msg.setText("Erro ao cadastrar, verifique se as informações foram preenchidadas corretamente ou se a empresa já não esta cadastrada!")
            msg.exec()
            db.close_connection()
            return
        
##################### buscar e exibe todas as empresas cadastradas na db ##############################

    def buscar_empresas(self):

        db = Data_base()
        db.connect()
        result = db.select_all_companies()

        self.ui.tbwl_empresas.clearContents()
        self.ui.tbwl_empresas.setRowCount(len(result))

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.ui.tbwl_empresas.setItem(row, column, QTableWidgetItem(str(data)))

        db.close_connection()


###################### atualiza os dados de empresas já cadastradas no banco de dados  ####################################


    def updata_company(self):

        dados = []
        update_dados = []

        for row in range(self.ui.tbwl_empresas.rowCount()):
            for column in range(self.ui.tbwl_empresas.columnCount()):
                dados.append(self.ui.tbwl_empresas.item(row, column).text())
        update_dados.append(dados)
        dados = []

        
        db = Data_base()
        db.connect() 

        for emp in update_dados:
            db.update_company(tuple(emp))

        db.close_connection()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Atualização de Dados")
        msg.setText("Dados atualizados com sucesso!")
        msg.exec()

        self.ui.tbwl_empresas.reset()
        self.buscar_empresas()

################################## Deletar empresas cadastradas do db ###############################

    def deletar_empresa(self):

        db = Data_base()
        db.connect()

        msg = QMessageBox()
        msg.setWindowTitle("Excluir")
        msg.setText("Este registor será excluído.")
        msg.setInformativeText("Você tem certeza que deseja excluir?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            cnpj = self.ui.tbwl_empresas.selectionModel().currentIndex().siblingAtColumn(0).data()
            result = db.delete_companies(cnpj)
            self.buscar_empresas()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("EMPRESAS")
            msg.setText(result)
            msg.exec()

        db.close_connection()
############################# gera um arquivo Excel a partir dos dados da tabela ########################################

    def gerar_excel(self):

        dados = []
        all_dados =  []

        for row in range(self.tb_company.rowCount()):
            for column in range(self.tb_company.columnCount()):
                dados.append(self.tb_company.item(row, column).text())
        
            all_dados.append(dados)
            dados = []

        columns = ['CNPJ', 'NOME', 'LOGRADOURO', 'NUMERO', 'COMPLEMENTO',
            'BAIRRO', 'MUNICÍPIO', 'UF', 'CEP','TELEFONE','EMAIL']
        
        empresas = pd.DataFrame(all_dados, columns= columns)
        empresas.to_excel("Empresas.xlsx", sheet_name='empresas', index=False)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Excel")
        msg.setText("Relatório Excel gerado com sucesso!")
        msg.exec()

############################### A rmazenadas dados do arquivo Excel em um db SQLite ####################################

    def gerar_excel_2(self):

        cnx = sqlite3.connect("system.db")

        empresas = pd.read_sql_query("""SELECT * FROM Empresas""", cnx)

        empresas.to_excel("Empresas.xlsx", sheet_name='empresas', index=False)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Excel")
        msg.setText("Relatório Excel gerado com sucesso!")
        msg.exec()


if __name__ == "__main__":

    db = Data_base()
    db.connect()
    db.create_table_company()
    db.close_connection()

    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    else:
        print("QApplication instance already exists")

    window = MainWindow()

    window.show() 
    app.exec()
