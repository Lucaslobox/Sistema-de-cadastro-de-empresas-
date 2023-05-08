# Sistema-de-cadastro-de-empresas-
Esse projeto é um sistema de cadastro de empresas cuja finalidade é cadastrar, excluir e atualizar as informações das empresas.   A tabela no programa exibe informações das empresas cadastradas na base de dados e pode ser exportada para o Excel, as informações preenchidas na interface gráfica são inseridas na base de dados.  

Video demosntrando projeto > https://www.loom.com/share/e5e41af3448349a9ac4cfd086e36d486


A R Q U I V O : main.py



Esse projeto é um sistema de cadastro de empresas que usa a biblioteca PySide6 para construir a interface gráfica. O projeto usa um tema personalizado, que é carregado de um arquivo .qss e tem funcionalidades de cadastrar, excluir e atualizar as informações das empresas. A tabela na interface exibe informações das empresas cadastradas na base de dados e pode ser exportada para o Excel. O projeto também possui uma funcionalidade para preencher automaticamente informações de endereço da empresa com base no CNPJ fornecido. O projeto também faz uso da API pública para buscar informações do CNPJ. As informações preenchidas na interface gráfica são inseridas na base de dados

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox, QTableWidgetItem)
from PySide6.QtCore import QFile, QTextStream
from ui_main import Ui_MainWindow
from PySide6 import QtCore
import sys
import pandas as pd
import sqlite3
from database import Data_base
from api_funtions import consulta_cnpj

Essas são as importações necessárias para o funcionamento do código.

QIcon é uma classe que permite carregar ícones que podem ser usados em janelas e botões.

QApplication é uma classe que gerencia o fluxo de eventos da interface gráfica.

QMainWindow é a classe base para as janelas principais do aplicativo.

QMessageBox é uma classe que exibe uma caixa de diálogo com uma mensagem e botões de ação.

QTableWidgetItem é uma classe que representa um item em uma tabela.

QFile é uma classe para manipulação de arquivos.

QTextStream é uma classe para leitura e escrita de dados em arquivos de texto.

Ui_MainWindow é a classe gerada pelo Qt Designer a partir do arquivo .ui da interface gráfica.

QtCore é um módulo que contém funcionalidades básicas do Qt.

sys é um módulo do Python que fornece acesso a algumas variáveis ​​usadas ou mantidas pelo interpretador e a funções que 
interagem fortemente com o interpretador.

pandas é uma biblioteca de análise de dados que fornece estruturas de dados para trabalhar com dados em tabelas e planilhas.

sqlite3 é uma biblioteca para interagir com bancos de dados SQLite.

Data_base (criada) é a classe criada para interagir com o banco de dados SQLite.

consulta_cnpj (criada) é a função que faz uma consulta à API pública de CNPJ para obter informações sobre uma empresa a partir do seu CNPJ.

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("BlackWolf - Sistema de cadastro de empresas")

A classe MainWindow é a janela principal da aplicação. Ela é definida como uma subclasse da classe QMainWindow e da classe gerada a partir do arquivo ui_main.py (que contém a interface gráfica da janela principal) chamada Ui_MainWindow.

No método __init__, que é o construtor da classe, é chamado o construtor das superclasses QMainWindow e Ui_MainWindow através da função super(), que permite chamar métodos e atributos da superclasse.

Em seguida, é criada uma instância da classe Ui_MainWindow e é chamado o método setupUi, que é responsável por configurar a interface gráfica da janela principal.

Por fim, é definido o título da janela principal através do método setWindowTitle.
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        app = QApplication.instance()
        qss_file_path = "C:/Users/Lucas Lobo/Desktop/projetos/cadastro_empresas/theme.qss"
        qss_file = QFile(qss_file_path)
        qss_file.open(QFile.ReadOnly | QFile.Text)
        stream = QTextStream(qss_file)
        qss = stream.readAll()

        app.setStyleSheet(qss)

Essa parte de código está carregando um arquivo .qss contendo as informações do estilo visual da aplicação e definindo-o como o estilo padrão da aplicação.

A variável "app" armazena a instância da aplicação, e a função "QApplication.instance()" retorna essa instância, caso ela já exista.

A variável "qss_file_path" armazena o caminho do arquivo .qss.

A variável "qss_file" abre o arquivo .qss em modo somente leitura e texto.

A variável "stream" lê todo o conteúdo do arquivo .qss.

A variável "qss" armazena o conteúdo do arquivo .qss.

Finalmente, a função "setStyleSheet(qss)" é usada para definir o estilo da aplicação com base nas informações contidas no arquivo .qss.

##################################### Sistema de botões - páginas ####################################################



        self.ui.btn_home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pg_home))
        self.ui.btn_cadastro.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_cadastro))
        self.ui.btn_Contatos.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pg_contatos))


        self.ui.btn_toggle.clicked.connect(self.container_menu)



Essa parte de código é responsável por criar a funcionalidade de trocar entre páginas do aplicativo quando os botões são clicados.

Ao clicar no botão "btn_home", o widget que será exibido será o "pg_home". O mesmo acontece com os botões "btn_cadastro" e "btn_contatos", onde o widget exibido será o "page_cadastro" e o "pg_contatos", respectivamente.

O botão "btn_toggle" é responsável por exibir ou ocultar o menu lateral do aplicativo, e é conectado a função 
"container_menu" para executar essa tarefa.

#########################  PREENCHER AUTOMATICAMENTE OS DADOS DO CNPJ ###############################


        self.ui.txt_cnpj.editingFinished.connect(self.consult_api)



Essa linha de código conecta o sinal editingFinished do QLineEdit chamado txt_cnpj ao método consult_api.

O sinal editingFinished é emitido quando o usuário termina de editar o texto no QLineEdit, seja por pressionar a tecla Enter, clicar fora do campo ou alterar o foco para outro widget.

Dessa forma, sempre que o usuário termina de editar o texto no txt_cnpj, a função consult_api é chamada automaticamente para fazer a consulta na API.

Essa linha de código conecta o sinal editingFinished do QLineEdit chamado txt_cnpj ao método consult_api.

O sinal editingFinished é emitido quando o usuário termina de editar o texto no QLineEdit, seja por pressionar a tecla Enter, clicar fora do campo ou alterar o foco para outro widget.

Dessa forma, sempre que o usuário termina de editar o texto no txt_cnpj, a função consult_api é chamada automaticamente para fazer a consulta na API.
        



##################################  Animação do Menu lateral #############################################   

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

Esta é uma função que controla a animação de expansão e contração de um contêiner de menu. Quando o botão "btn_toggle" é clicado, a largura atual do contêiner é verificada. Se a largura atual for 9 (o que significa que o contêiner está recolhido), a nova largura é definida como 200. Caso contrário, a nova largura é definida como 9 (o que significa que o contêiner será recolhido novamente).

A função, então, cria uma instância de QPropertyAnimation, que é uma classe que permite animar as propriedades dos widgets, e define a duração da animação, a largura inicial (a largura atual do contêiner), a largura final (a nova largura) e a curva de animação a ser usada. Em seguida, inicia a animação usando o método start().


############################ Função de consultar uma API e atribuição aos campos correspondentes ###########################

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

Essa função "consult_api" é definida dentro de uma classe em Python e recebe o objeto "self" como um parâmetro implícito.

A função é responsável por consultar uma API para obter informações com base no CNPJ fornecido pelo usuário na interface gráfica do programa. Essa consulta é realizada pela chamada da função "consulta_cnpj" que recebe o CNPJ como argumento e retorna uma lista com várias informações relacionadas à empresa, como nome empresarial, endereço, telefone, email, entre outros.

Em seguida, a função "consult_api" 
na interface gráfica do programa, utilizando o método "setText" de cada campo. Por exemplo, o nome empresarial é atribuído ao campo "txt_nmempresarial", o endereço é atribuído aos campos "txt_logradouro", "txt_numero" e "txt_complemento", e assim por diante.

Note que a função também realiza algumas operações de formatação nas informações obtidas da API, como remover pontos e traços do CEP e do telefone antes de atribuí-los aos campos correspondentes.



################################ cadastrar informações da empresa na base de dados #########################################


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

Essa função "cadastrar_empresas" é definida dentro de uma classe em Python e recebe o objeto "self" como um parâmetro implícito.

A função é responsável por cadastrar as informações da empresa na base de dados, utilizando os valores fornecidos pelo usuário na interface gráfica do programa. Para isso, a função cria uma instância da classe "Data_base" e chama o método "connect()" para estabelecer uma conexão com a base de dados.

Em seguida, a função cria uma tupla chamada "fullDataSet" que contém todos os valores dos campos da interface gráfica do programa. Cada valor é extraído do campo correspondente na interface gráfica por meio do método "text()", que retorna o texto atual do campo como uma string. Note que, no caso do campo "txt_telefone", a função também chama o método "strip()" para remover quaisquer espaços em branco desnecessários no início ou no final da string.

A função então chama o método "register_company" da instância da classe "Data_base", passando a tupla "fullDataSet" como argumento. Esse método é responsável por inserir as informações da empresa na base de dados. A função verifica se o retorno do método "register_company" é igual a "OK", o que indica que o cadastro foi realizado com sucesso. Em caso positivo, a função exibe uma mensagem de sucesso por meio de um objeto "QMessageBox" e encerra a conexão com a base de dados, retornando imediatamente. Caso contrário, a função exibe uma mensagem de erro indicando que as informações fornecidas pelo usuário podem estar incorretas ou que a empresa já está cadastrada na base de dados.


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


Essa função "buscar_empresas" é definida dentro de uma classe em Python e recebe o objeto "self" como um parâmetro implícito.

A função é responsável por buscar todas as empresas cadastradas na base de dados e exibi-las em uma tabela na interface gráfica do programa. Para isso, a função cria uma instância da classe "Data_base" e chama o método "connect()" para estabelecer uma conexão com a base de dados.

Em seguida, a função chama o método "select_all_companies" da instância da classe "Data_base", que é responsável por recuperar todas as empresas cadastradas na base de dados. O resultado da consulta é armazenado na variável "result".

A função então limpa o conteúdo atual da tabela na interface gráfica do programa por meio do método "clearContents()" do objeto "tbwl_empresas", que é um objeto "QTableWidget" da biblioteca PyQt5. A função define o número de linhas da tabela para o tamanho da lista "result" por meio do método "setRowCount()" do objeto "tbwl_empresas".

Em seguida, a função percorre cada elemento da lista "result" por meio de um laço "for". Para cada elemento, a função define um item na tabela por meio do método "setItem()" do objeto "tbwl_empresas", especificando a linha e a coluna do item e o valor do item como uma string convertida a partir do valor original usando a função "str()".

Portanto, após a execução da função, a tabela na interface gráfica do programa exibirá todas as empresas cadastradas na base de dados, com seus respectivos dados distribuídos em linhas e colunas da tabela.

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


Primeiro, a função cria duas listas vazias: dados e update_dados. Em seguida, ela itera sobre as linhas e colunas da tabela que exibe as informações das empresas cadastradas (self.ui.tbwl_empresas) e adiciona o texto de cada célula à lista dados. Após iterar sobre todas as células da tabela, a lista dados é adicionada à lista update_dados como um elemento.

Depois disso, a função cria uma conexão com o banco de dados usando a classe Data_base(), e itera sobre a lista update_dados, atualizando as informações de cada empresa no banco de dados por meio do método update_company(). Após atualizar as informações de todas as empresas, a conexão com o banco de dados é fechada.

Em seguida, a função exibe uma mensagem informando que a atualização foi realizada com sucesso, e reseta a tabela de exibição de empresas e atualiza-a novamente com os dados atualizados.



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


Essa função "deletar_empresa" é responsável por excluir um registro de empresa do banco de dados.

Primeiro, a função se conecta ao banco de dados. Em seguida, exibe uma caixa de diálogo para confirmar a exclusão do registro selecionado na tabela de empresas. Se o usuário confirmar, o número do CNPJ é obtido a partir do registro selecionado na tabela e, em seguida, a função "delete_companies" do objeto db (instância da classe Data_base) é chamada para executar a exclusão do registro do banco de dados.

Depois que o registro é excluído com sucesso, a função chama a função "buscar_empresas" para atualizar a tabela de empresas exibida na interface do usuário. Por fim, é exibida uma mensagem informando se a exclusão foi concluída com sucesso ou se houve algum erro. Por fim, a função fecha a conexão com o banco de dados.

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

Primeiro, a função percorre a tabela (self.tb_company) e adiciona cada célula em uma lista (dados). Quando chega ao final de uma linha, essa lista é adicionada a outra lista (all_dados), que contém todos os dados da tabela.

Em seguida, é definida uma lista de nomes de colunas (columns) e é criado um DataFrame do pandas (empresas) com as informações contidas em all_dados e as colunas definidas anteriormente. Então, é utilizado o método to_excel para salvar os dados em um arquivo Excel com nome "Empresas.xlsx", na aba "empresas", sem indexação.

Por fim, é exibida uma mensagem informando que o relatório Excel foi gerado com sucesso.


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


Essa função tem como objetivo gerar um arquivo Excel contendo as informações das empresas armazenadas em um banco de dados SQLite.

Primeiro, a função estabelece uma conexão com o banco de dados usando a biblioteca sqlite3. Em seguida, ela usa o método read_sql_query do pandas para executar uma consulta SQL na tabela de Empresas do banco de dados e carregar os resultados em um DataFrame.

Após isso, a função utiliza o método to_excel do pandas para gerar um arquivo Excel com o nome "Empresas.xlsx", contendo uma planilha chamada "empresas" e as informações das empresas armazenadas no DataFrame. A opção index=False é usada para evitar que o índice do DataFrame seja incluído no arquivo Excel.

Por fim, a função exibe uma mensagem de confirmação para o usuário, informando que o relatório Excel foi gerado com sucesso.

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


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


A linha if __name__ == "__main__": verifica se o módulo está sendo executado como um programa principal, ou se está sendo importado como um módulo em outro programa.

Dentro do bloco condicional, primeiro é criado um objeto Data_base, que conecta ao banco de dados, cria a tabela se ela ainda não existir, e em seguida fecha a conexão.

Em seguida, o programa verifica se uma instância de QApplication já existe. Se sim, a instância existente é usada, caso contrário, uma nova instância é criada.

Por fim, a janela principal é criada e exibida, e a execução do aplicativo é iniciada com app.exec(). Isso mantém o aplicativo em execução até que o usuário o feche.


----------------------------------------------------------------------------------------------------------------------------



 							A R Q U I V O : api_functions


import requests
import json

def consulta_cnpj(cnpj):

    url = f"https://www.receitaws.com.br/v1/cnpj/{cnpj}"
    querystring = {"token":"XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX","cnpj":"06990590000123","plugin":"RF"}
    response = requests.request("GET", url, params=querystring)

    resp = json.loads(response.text)


    return resp['nome'], resp['logradouro'], resp['numero'], resp['complemento'], resp['bairro'], resp['municipio'], resp['uf'], resp['cep'], resp['telefone'], resp['email']


Esta é uma função chamada consulta_cnpj que utiliza as bibliotecas requests e json para realizar uma requisição a uma API para consultar informações sobre um determinado CNPJ.

A função recebe um parâmetro cnpj que é o número do CNPJ a ser consultado.

A variável url é criada a partir de uma string formatada com o número do CNPJ recebido como parâmetro. A variável querystring é um dicionário contendo os parâmetros da requisição, no caso, o token de acesso, o CNPJ a ser consultado e um plugin específico.

A função utiliza a biblioteca requests para fazer uma requisição HTTP GET à URL construída anteriormente, passando os parâmetros da consulta na variável querystring. O resultado é armazenado na variável response.

O conteúdo da resposta é um objeto JSON, então a função utiliza a biblioteca json para carregar a resposta da API em um objeto Python, armazenado na variável resp.

Por fim, a função retorna uma tupla contendo diversas informações relacionadas ao CNPJ consultado, como nome, endereço, telefone e email, extraídas do objeto JSON retornado pela API.
----------------------------------------------------------------------------------------------------------------------------



 							A R Q U I V O : database



Essa é uma classe em Python que define um objeto de conexão com um banco de dados SQLite. A classe inclui vários métodos que permitem a criação de tabelas, inserção, seleção, atualização e exclusão de dados na tabela "Empresas". Os métodos incluem "create_table_company", "register_company", "select_all_companies", "delete_companies" e "update_company". Cada método é responsável por realizar uma operação específica na tabela e utiliza a linguagem SQL para executar as consultas no banco de dados. A classe utiliza a biblioteca SQLite3, que é uma biblioteca integrada ao Python que permite a comunicação com bancos de dados SQLite.


////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

import sqlite3

O módulo sqlite3 é um módulo nativo do Python que permite interagir com bancos de dados SQLite usando o Python. SQLite é um banco de dados relacional que é armazenado em um arquivo local e é usado principalmente para aplicativos de desktop e móveis. O módulo sqlite3 fornece uma API para criar, ler, atualizar e excluir registros de um banco de dados SQLite usando Python.

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

class Data_base:

    def __init__(self, name = 'system.db') -> None:        
        self.name = name


Esta é uma classe em Python chamada Data_base. Ela é utilizada para criar um objeto que representa uma conexão com um banco de dados SQLite.

O construtor da classe é definido pela função __init__. Ela tem um parâmetro name com valor padrão 'system.db'. Se nenhum argumento for passado ao criar um objeto da classe, o nome do banco de dados será 'system.db'. Caso contrário, o nome passado como argumento será utilizado.

O construtor da classe armazena o nome do banco de dados na variável de instância self.name. Isso permite que outras funções da classe tenham acesso ao nome do banco de dados que está sendo utilizado.

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

###################################### cria uma conexão com um banco de dados ####################################

def connect(self):
        self.connection = sqlite3.connect(self.name)


A função connect cria uma conexão com um banco de dados SQLite. Ela utiliza a biblioteca sqlite3 para se conectar com um banco de dados e retorna um objeto de conexão.

O método connect é parte de uma classe que tem a responsabilidade de encapsular as operações do banco de dados, oferecendo uma interface para que outras partes do programa possam realizar operações como adicionar, remover e atualizar dados.

Neste caso o método connect é utilizado para criar uma conexão com o banco de dados SQLite, que é especificado pelo parâmetro self.name. O objeto de conexão é armazenado em self.connection, permitindo que outros métodos da classe acessem e utilizem essa conexão para realizar operações no banco de dados.


#################################### Fecha conexão com db ##########################################################


    def close_connection(self):
        try:
            self.connection.close()
        except:
            pass

A função close_connection é um método da classe Data_base que fecha a conexão com o banco de dados. Ela utiliza o método close() da biblioteca sqlite3 para fechar a conexão. A função é protegida por um bloco try-except para garantir que, caso ocorra algum erro durante o fechamento da conexão, o programa não pare de funcionar. Se ocorrer algum erro, o bloco except simplesmente ignora o erro e o programa continua a ser executado.



############################################# Cria tabela Empresas ####################################################

def create_table_company(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Empresas(

            CNPJ TEXT,
            NOME TEXT,
            LOGRADOURO TEXT,
            NUMERO TEXT,
            COMPLEMENTO TEXT,
            BAIRRO TEXT,
            MUNICIPIO TEXT,
            UF TEXT,
            CEP TEXT,
            TELEFONE TEXT,
            EMAIL TEXT,

            PRIMARY KEY(CNPJ)
            );
 
        """)


Essa é uma função que cria uma tabela chamada "Empresas" com as colunas "CNPJ", "NOME", "LOGRADOURO", "NUMERO", "COMPLEMENTO", "BAIRRO", "MUNICIPIO", "UF", "CEP", "TELEFONE" e "EMAIL" no banco de dados SQLite.

A função usa a conexão com o banco de dados criada anteriormente e cria um cursor, que é usado para executar a instrução SQL para criar a tabela.

A cláusula "IF NOT EXISTS" é usada para verificar se a tabela já existe no banco de dados antes de criá-la, evitando assim que ocorram erros.

A coluna "CNPJ" é definida como chave primária da tabela, o que significa que cada registro da tabela deve ter um valor exclusivo na coluna "CNPJ".

######################################### Registra empresas no db SQLit ##################################################

    def register_company(self, fullDataSet):

        campos_tabela = ('CNPJ','NOME','LOGRADOURO','NUMERO','COMPLEMENTO','BAIRRO','MUNICIPIO','UF','CEP','TELEFONE','EMAIL')

        qntd = ("?,?,?,?,?,?,?,?,?,?,?")
        cursor = self.connection.cursor()

        try:
            cursor.execute(f"""INSERT INTO Empresas {campos_tabela}
            VALUES({qntd})""", fullDataSet)
            self.connection.commit()
            return("OK")

        except:
            return "Erro"

A função register_company recebe como parâmetro uma tupla fullDataSet que contém as informações da empresa a serem inseridas no banco de dados. A função começa criando uma string chamada qntd com 11 interrogações separadas por vírgulas, correspondendo aos 11 campos da tabela. Em seguida, o cursor é criado e a função tenta executar um comando SQL de inserção de dados na tabela Empresas com a tupla fullDataSet passada como parâmetro. A string campos_tabela define os campos que devem ser inseridos na tabela. Se a inserção for bem sucedida, a função confirma a transação e retorna a string "OK". Caso contrário, ela retorna a string "Erro".


################################### Seleciona e retorná em ordem alfabética ################################################


def select_all_companies(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Empresas ORDER BY NOME")
            empresas = cursor.fetchall()
            return empresas
        except:
            pass


Essa função chamada select_all_companies tem como objetivo selecionar todas as empresas registradas na tabela "Empresas" do banco de dados e retorná-las em ordem alfabética pelo nome.

Para isso, a função utiliza o método execute para executar uma consulta SQL que seleciona todos os campos da tabela "Empresas". Em seguida, utiliza o método fetchall para buscar todas as linhas retornadas pela consulta e armazená-las na variável empresas.

Por fim, a função retorna a variável empresas que contém a lista com todas as empresas registradas na tabela "Empresas" em ordem alfabética pelo nome. Se ocorrer algum erro durante a execução da consulta SQL ou recuperação das linhas, a função retorna None.

######################################### Deleta dado sobre empresas ######################################################

def delete_companies(self, id):

        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM Empresas WHERE CNPJ = '{id}' ")

            self.connection.commit()

            return "Cadastro de empresa excluido com sucesso!"

        except:
            return "Erro ao Excluir registro!"


A função delete_companies recebe um parâmetro id que representa o CNPJ da empresa a ser excluída. Dentro da função, é feita uma tentativa de se conectar ao banco de dados e obter um cursor. Em seguida, é executado um comando SQL que deleta o registro da tabela Empresas que corresponde ao CNPJ fornecido.

Se a operação for bem sucedida, ou seja, se o registro foi excluído do banco de dados, a função retorna uma mensagem de sucesso. Caso contrário, a função retorna uma mensagem de erro.


############################  Atualiza os dados de uma empresa existente na tabela   ######################################

    def update_company(self, fullDataSet):

        cursor = self.connection.cursor()
        cursor.execute(f""" UPDATE Empresas set

            CNPJ = '{fullDataSet[0]}',
            NOME = '{fullDataSet[1]}',
            LOGRADOURO = '{fullDataSet[2]}',
            NUMERO = '{fullDataSet[3]}',
            COMPLEMENTO = '{fullDataSet[4]}',
            BAIRRO = '{fullDataSet[5]}',
            MUNICIPIO = '{fullDataSet[6]}',
            UF = '{fullDataSet[7]}',
            CEP = '{fullDataSet[8]}',
            TELEFONE = '{fullDataSet[9]}',
            EMAIL = '{fullDataSet[10]}'

            WHERE CNPJ = '{fullDataSet[0]}'""")

        self.connection.commit()

Esta função atualiza os dados de uma empresa existente na tabela de empresas da base de dados. Recebe como entrada um conjunto completo de dados (fullDataSet) para atualizar as informações da empresa.

A função primeiro cria um cursor para a conexão com a base de dados, em seguida, executa uma instrução SQL UPDATE para atualizar os dados da empresa. A cláusula WHERE é usada para identificar a empresa correta que será atualizada.

Por fim, a função confirma a transação e fecha o cursor.
