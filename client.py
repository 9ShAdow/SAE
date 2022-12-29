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
cpu = psutil.cpu_count()
name =("")
ip = socket.gethostbyname(name)
host = "localhost"
#netifaces.interfaces()
stockage = ("")
#adresse_ip = netifaces.ifaddresses('en0')[2][0]['addr'] # en0 = ethernet,si votre adresse ip est sur une autre interface il faudra changer "en0" par le nom de l'interface
#netaddr_adresse_ip = netaddr.IPAddress(adresse_ip)
stockage = shutil.disk_usage("/")
help =""


port = 7000





class client(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SAE 302")
        grid = QGridLayout()
        widget = QWidget()
        self.setCentralWidget(widget)
        widget.setLayout(grid)
        self.resize(537, 250)

        rama = QPushButton("RAM")
        cpuu = QPushButton("CPU")
        ipp = QPushButton("IP")
        oss = QPushButton("OS")
        namee = QPushButton("NAME")
        #pingg = QPushButton("Ping")
        #porto= QPushButton("Port")
        #disque = QPushButton("Disque")
        quitter = QPushButton("Quit")
        self.label = QTextEdit("")
        help = QPushButton("Help")
        clear = QPushButton("clear")
        envoyer = QPushButton("Envoyer")
        self.__conn = QPushButton("connect")
        #en = QLabel("Entrer votre commande")
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
        }""")

        #quitter.setStyleSheet("color: #db7093")
        #self.__conn.setStyleSheet("color: white")
        #self.__conn.setStyleSheet("border-radius: 10px ,")

#PARTIE GRID
    
        grid.addWidget(rama, 0, 0)
        grid.addWidget(cpuu, 1, 0)
        grid.addWidget(ipp, 2, 0)
        grid.addWidget(oss, 3, 0)
        grid.addWidget(namee, 4, 0)
        grid.addWidget(self.__conn,5,0)
        #grid.addWidget(pingg, 5, 0)
        #grid.addWidget(porto, 9, 0)
        #grid.addWidget(disque, 6, 0)
        grid.addWidget(quitter, 0  ,12)
        grid.addWidget(clear, 5,12)
        grid.addWidget(self.label, 0, 1, 5, 11)
        grid.addWidget(help,1,12)
        grid.addWidget(envoyer, 5, 11)
        grid.addWidget(self.__input,  5,1,1,10)
        
#PARTIE DES ACTIONS

        rama.clicked.connect(self.__actionram)
        cpuu.clicked.connect(self.__actioncpu)
        ipp.clicked.connect(self.__actionip)
        oss.clicked.connect(self.__actionos)
        namee.clicked.connect(self.__actionname)
        #porto.clicked.connect(self.__actionport)
        #pingg.clicked.connect(self.__actionping)
        #disque.clicked.connect(self.__actiondisque)
        envoyer.clicked.connect(self.__actionenvoyer)
        quitter.clicked.connect(self.__actionquitter)
        envoyer = QShortcut(QKeySequence("Return"), self)
        envoyer.activated.connect(self.__actionenvoyer)
        help.clicked.connect(self.__actionhelp)
        clear.clicked.connect(self.__actionclear)
        #btn.clicked.connect(self.__actionbtn)

#PARTIE FONCTION
    #def __actionenvoyer(self):

    def __actionenvoyer(self):
        message = self.__input.text()
        client_socket.send(message.encode())
        print("La requête a été envoyée")
        data = client_socket.recv(1024).decode()
        
        print(f"Message du serveur : {data}")
        self.label.append(f"{data}\n")
        self.__actionreinitialiser()

    def __actionreinitialiser(self):
        self.__input.clear()
        self.__input.setPlaceholderText("Entrez la prochaine commande")
    
    

  
    
    

    def __actionquitter(self):
        self.close()



    


    def __actionclear(self):
        self.label.clear()
        self.label.append("")

    def __actionhelp(self):
        message = QMessageBox()
        message.setText("Commande disponible:\n \n - La commande ram permet d'afficher la ram totale, la ram utilisée et la ram libre \
            \n \n - La commande ip permet d'afficher l'adresse ip de la machine \
            \n \n  - La commande os permet d'afficher le nom et la version de l'os\
            \n \n - La commande name permet d'afficher le nom de la machine\
            \n \n - La commande port permet d'afficher le port utilisé  \
            \n \n - La commande cpu permet d'afficher le nombre de coeur de la machine \
            \n \n - La commande disque permet d'afficher le stockage total, le stockage utilisé et le stockage libre")
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
        
  






if __name__ == "__main__":

    print(f"Ouverture de la socket sur le serveur {host} port {port}")
    client_socket = socket.socket()
    client_socket.connect((host, port))
    print("Serveur est connecté")

    app = QApplication(sys.argv)
    window = client()
    window.show()
    app.exec()
