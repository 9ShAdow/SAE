from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import socket
import sys
import psutil
#import netifaces
import netaddr
import shutil
from PyQt6.QtGui import QShortcut, QKeySequence
 



os = ("")
cpu = int(psutil.cpu_count())
ram = int(psutil.virtual_memory().percent)
name =("")
ip = socket.gethostbyname(name)

#netifaces.interfaces()
stockage = ("")
#adresse_ip = netifaces.ifaddresses('en0')[2][0]['addr'] # en0 = ethernet,si votre adresse ip est sur une autre interface il faudra changer "en0" par le nom de l'interface
#netaddr_adresse_ip = netaddr.IPAddress(adresse_ip)
stockage = shutil.disk_usage("/")
help =""
'''def __actionlireservX(self):
    liretxt = open("servX.txt", "r")
    txt = liretxt.read()
    txt = liretxt.split(";")
    host = txt[0]
    port = txt[1]

    

    liretxt.close()
    return txt'''

host = "localhost"

port = 7000

'''liretxt = open("servX.txt", "r")
txt = liretxt.read()
txt = liretxt.split("\n")
liretxt.close()'''






class client(QMainWindow):
    def __init__(self):
        
        '''self.clsocket = socket.socket()
        self.message = ''
        self.iskilled = False
        self.__affichage = affichage

    def connexion(self, host, port):
        self.clsocket.connect((host, port))
        thread = threading.Thread(target=self.reception)
        thread.start()'''
        super().__init__()
        self.setWindowTitle("SAE 302")
        grid = QGridLayout()
        widget = QWidget()
        self.setCentralWidget(widget)
        widget.setLayout(grid)
        self.resize(537, 250)

        ram = QPushButton("RAM")
        cpuu = QPushButton("CPU")
        ipp = QPushButton("IP")
        oss = QPushButton("OS")
        namee = QPushButton("NAME")
        quitter = QPushButton("Quit/KILL")
        reset = QPushButton("Reset")
        disconnect = QPushButton("Disconnect")
        self.label = QTextEdit("")
        help = QPushButton("Help")
        clear = QPushButton("clear")
        infom = QPushButton("Info Memoire")	
        envoyer = QPushButton("Envoyer")
        self.__conn = QPushButton("connect")
        informations = QPushButton("Informations")
        self.__input = QLineEdit() 
        self.__input.setMaxLength(100)
        self.__input.setPlaceholderText("Entrez votre commande")



#style css de l'interface
 
        with open("styles.css","r") as file:
            app.setStyleSheet(file.read())
            


        self.__conn.setStyleSheet("""
        QPushButton {
            color: #ffc0cb;
        }
        QPushButton:hover {
            color: #db7093;
        }
        """)

        clear.setStyleSheet("""
        QPushButton {
            color: #ffc0cb;
        }
        QPushButton:hover {
            color: #db7093;
        }
        """)
        quitter.setStyleSheet("""
        QPushButton {
            color: #ffc0cb;
        }
        QPushButton:hover {
            color: #db7093;
        }
        """)

    

    #modifier la scrollbar
        self.label.setStyleSheet("""
        QScrollBar:vertical {
            width: 10px;
            background-color: #3d3d3d;
        }
        QScrollBar::handle:vertical {
            background: #3d3d3d;
            border-radius: 5px;
            border: 1px solid;
        }
        QScrollBar::add-line:vertical {
            background: #ffc0cb;
            height: 0px;
            subcontrol-position: top;
            subcontrol-origin: margin;
        }
        """)

       
#ajouter une addresse et un port dans servX.txt


        
      

#PARTIE GRID
    
        grid.addWidget(ram, 0, 0)
        grid.addWidget(cpuu, 1, 0)
        grid.addWidget(ipp, 2, 0)
        grid.addWidget(oss, 3, 0)
        grid.addWidget(namee, 4, 0)
        grid.addWidget(self.__conn,5,0)
        grid.addWidget(informations, 4,12)
        grid.addWidget(infom, 3,12)
        grid.addWidget(quitter, 0  ,12)
        grid.addWidget(reset, 1,12)
        grid.addWidget(disconnect, 2,12)
        grid.addWidget(clear, 5,12)
        grid.addWidget(self.label, 0, 1, 5, 11)
        grid.addWidget(help,1,12)
        grid.addWidget(envoyer, 5, 11)
        grid.addWidget(self.__input,  5,1,1,10)

        
#PARTIE DES ACTIONS

        ram.clicked.connect(self.__actionram)
        cpuu.clicked.connect(self.__actioncpu)
        ipp.clicked.connect(self.__actionip)
        oss.clicked.connect(self.__actionos)
        namee.clicked.connect(self.__actionname)
        envoyer.clicked.connect(self.__actionenvoyer)
        quitter.clicked.connect(self.__actionquitter)
        reset.clicked.connect(self.__actionresetserver)
        infom.clicked.connect(self._actionInfos)

        #restart.clicked.connect(self.__actionrestart)
        #disconnect.clicked.connect(self.__actiondisconnect)
        informations.clicked.connect(self.__actioninformations)
        envoyer = QShortcut(QKeySequence("Return"), self)
        envoyer.activated.connect(self.__actionenvoyer)
        historique = QShortcut(QKeySequence("up"), self)
        historique.activated.connect(self.__uphistorique)
        help.clicked.connect(self.__actionhelp)
        clear.clicked.connect(self.__actionclear)
        #btn.clicked.connect(self.__actionbtn)

#PARTIE FONCTION
    
    def __actionresetserver(self):
        #reset du serveur
        client_socket.send("reset".encode())
        client_socket.close()
        self.label.append("Le serveur a été reset")
        print('Reset du serveur')

        




    def disconnect(self):
        self.iskilled = True
        client_socket.send("disconnect".encode())
        client_socket.close()
        print('Deconnexion du client')


    def __actioninformations(self):
        #informations : ip et nom de la machine
        self.label.append("Le nom de la machine : " + socket.gethostname())
        self.label.append("L'adresse IP : " + socket.gethostbyname(socket.gethostname()))
        

    def __actionenvoyer(self):
        message = self.__input.text() 

        '''if message == "" or message == " " or message.startswith(" "):
            self.__input.setText("")
            self.__input.setPlaceholderText("ERREUR DE SAISIE !")'''
        if message == "" or message == " " or message.startswith(" "):
            self.__input.setText("")
            self.__input.setPlaceholderText("ERREUR DE SAISIE !")
        elif message == "help":
            client_socket.send(message.encode())
            self.label.append("help : Affiche la liste des commandes disponibles\n")
            self.label.append("clear : Efface l'historique des commandes\n")
            self.label.append("quit : Quitte le client\n")
            self.label.append("restart : Redémarre le serveur\n")
            self.label.append("disconnect : Déconnecte le client du serveur\n")
            self.label.append("ram : Affiche l'utilisation de la RAM\n")
            self.label.append("cpu : Affiche l'utilisation du CPU\n")
            self.label.append("ip : Affiche l'adresse IP du serveur\n")
            self.label.append("os : Affiche le nom de l'OS\n")
            self.label.append("name : Affiche le nom du serveur\n")
            self.label.append("port : Affiche le port du serveur\n")
            self.label.append("ping : Affiche le ping du serveur\n")
            self.label.append("disk : Affiche l'utilisation du disque dur\n")
            self.__actionreinitialiser()
        elif message == "clear":
            self.label.setText("")
            self.__actionreinitialiser()
        elif message == "quit" or message == "exit" or message == "kill":

            self.close()
        else:
            message = self.__input.text()
            client_socket.send(message.encode())

            print("La requête a été envoyée")
            data = client_socket.recv(1024).decode()
        
    
            print(f"Message du serveur : {data}")
            self.label.append(f"{data}")
            self.__actionreinitialiser()
        
        
    
    def __uphistorique(self):
        message = "dercommande"
        client_socket.send(message.encode())
        print("La requête pour la ram a été envoyée")

        data = client_socket.recv(1024).decode()
        print(f"Message du serveur : {data}")
        
        #self.__label.append(f"{data}")

        #self.__input.setPlaceholderText(f"{data}")
        



    def __actionreinitialiser(self):
        self.__input.clear()
        self.__input.setPlaceholderText("Entrez la prochaine commande")
    
    

  
    
    

    def __actionquitter(self):
        self.close()
    
    '''def __actionrestart(self):
        os.system("python3 client.py")
        self.close()'''




    


    def __actionclear(self):
        self.label.clear()
        self.label.append("")

    def __actionhelp(self):
        message = QMessageBox()
        message.setText("Commande disponible:\n \n - La commande ram permet d'afficher la ram totale, la ram utilisée et la ram libre \
            \n \n - La commande ip permet d'afficher l'adresse ip de la machine \
            \n \n  - La commande os permet d'afficher le nom et la version de l'os\
            \n \n - La commande name permet d'afficher le nom de la machine\
            \n \n - La commande cpu permet d'afficher les statistiques du cpu \
            \n \n - La commande mkdir permet de créer un dossier ")
        message.exec()   
    

    def __actionram(self):
        message = "ram"
        client_socket.send(message.encode())
        print("La requête pour la ram a été envoyée")
        data = client_socket.recv(1024).decode()
        print(f"Message du serveur : Voici vos statistiques sur la ram{data}")
        self.label.append(f"{data}\n")
        


    def __actionip(self):
        message = "ip"
        client_socket.send(message.encode())
        print("La requête pour l'ip a été envoyée")
        data = client_socket.recv(1024).decode()
        print(f"Message du serveur : Votre ip est {data}")
        self.label.append(f"{data} \n")
    
    def __actionos(self):
        message = "os"
        client_socket.send(message.encode())
        print("La requête pour l'os a été envoyée")
        data = client_socket.recv(1024).decode()
        print(f"Message du serveur : Vous êtes sur l'OS  {data}")
        self.label.append(f"{data} \n")
        
    
    def __actionname(self):
        message = "name"
        client_socket.send(message.encode())
        print("La requête pour le nom a été envoyée")
        data = client_socket.recv(1024).decode()
        print(f"Message du serveur : Le nom de votre machine est  {data}")
        self.label.append(f"{data} \n")
    

   
    def __actioncpu(self):
        message="cpu"
        client_socket.send(message.encode())
        print("La requête pour le cpu a été envoyée")
        data = client_socket.recv(1024).decode()
        print(f"Message du serveur : Le cpu est utilisé à {data} %")
        self.label.append(f"{data} \n")

    def _actionInfos(self):
        diag = Infosmem()
        diag.show()
        diag.exec()
    


class Infosmem(QDialog):
    def __init__(self):
            super().__init__()
            self.setWindowTitle("Utilisation de la memoire")
            self.resize(250, 125)

            self.__cpubar = QProgressBar()
            self.__cpubar.setValue(cpu)
            self.__cpubar.setFormat("CPU : %p%")
            self.__cpubar.setStyleSheet("""
            QProgressBar::chunk {
                background-color: #ffc0cb;
                padding-top: 1px;
            }
            QProgressBar:hover {
                border: 1px solid #000000;
                border-radius: 5px;
                text-align: center;
            """)
            self.__cpubar.setTextVisible(True)
            self.__rambar = QProgressBar()
            
            self.__rambar.setValue(ram)
            self.__rambar.setFormat("RAM : %p%")
            self.__rambar.setStyleSheet("""
            QProgressBar::chunk {
                background-color: #ffc0cb;
                padding-top: 1px;
            }
            """)

            #self.__rambar.setOrientation(Qt.Horizontal)
            self.__rambar.setTextVisible(True)
            

            self.__grid = QGridLayout()
            self.setLayout(self.__grid)
            self.__grid.addWidget(self.__cpubar, 0, 0, 1, 1)
            self.__grid.addWidget(self.__rambar, 1, 0, 1, 1)
           

  






if __name__ == "__main__":

    print(f"Ouverture de la socket sur le serveur {host} port {port}")
    client_socket = socket.socket()
    client_socket.connect((host, port))
    print("Serveur est connecté")

    app = QApplication(sys.argv)
    window = client()
    window.show()
    app.exec()
