import socket
import  os 
import psutil
import platform
from PyQt6.QtWidgets import *
from PyQt6.QtCore import * 
import sys
from requests import Session
#on va faire un ficher pour lancer tt les serveurs en meme temps ensuite en fonction des num on pourra choisir le serveur
"""
client_socket = socket.socket()
print("Socket créé.")
host = "localhost"
port = input("Choisissez le serveur de connexion : ")

if port == "1":
    port = 1111
elif port == "2":
    port = 10000
else:
    print("Serveur introuvable !")

client_socket.connect((host, port))
print("Connecté au serveur.")
message =input("envoi d'un message : ")
client_socket.send(message.encode())
print("Message envoyé")
"""




class client(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Client")
        grid = QGridLayout()
        widget = QWidget()
        self.setCentralWidget(widget) 
        widget.setLayout(grid)
        self.label = QTextEdit()
        

        name = 'shad' # Enter your name here!
        chat_url = 'https://build-system.fman.io/chat'
        server = Session()

        ram= QPushButton("ram")
        cpu=QPushButton("cpu")
        name=QPushButton("name")
        
        #ok#
        text_area = QTextEdit()
        text_area.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        message = QLineEdit()
        layout = QVBoxLayout()
        layout.addWidget(text_area)
        layout.addWidget(message)

        #evenement

        # Event handlers:
        def display_new_messages():
            new_message = server.get(chat_url).text
            if new_message:
                text_area.append(new_message)

        def send_message():
            server.post(chat_url, {'name': name, 'message': message.text()})
            message.clear()

        # Signals:
        message.returnPressed.connect(send_message)
        timer = QTimer()
        timer.timeout.connect(display_new_messages)
        timer.start(1000)

        

        


        grid.addWidget(ram, 0, 0)
        grid.addWidget(cpu , 1, 0)
        grid.addWidget(name, 2, 0)
        grid.addWidget(text_area, 0, 1, 3, 1)
        grid.addWidget(message, 3, 0, 1, 2)
        
    

        ram.clicked.connect(self.__actionram)
        cpu.clicked.connect(self.__actioncpu)
        name.clicked.connect(self.__actionname)
        

        #on essaye

        
        #on essaye 


    def __actionram(self):
        message = "ram"
        client_socket.send(message.encode())
        print("La requête pour la ram a été envoyée")
        data = client_socket.recv(1024).decode()
        
        print(f"Message du serveur : {data}")
        self.label.append(f"{data}\n")
        self.label.append(f"")
        
        
   

    def __actioncpu(self):
        message = "cpu"
        client_socket.send(message.encode())
        print("La requête pour la cpu a été envoyée")
        data = client_socket.recv(1024).decode()
        print(f"Message du serveur : {data}")
        self.label.append(f"{data}\n")

    def __actionname(self):
        message = "name"
        client_socket.send(message.encode())
        print("La requête pour le nom a été envoyée")
        data = client_socket.recv(1024).decode()
        print(f"Message du serveur : {data}")
        self.label.append(f"{data}\n")

"""
if message == "arret" or message == "bye":
    print("Connexion terminé.")
    client_socket.close()

elif message == "ram":
    __actionram(self)
elif message == "cpu":
    __actioncpu(self)   
else:
    data = client_socket.recv(1024).decode()
    '''print("Message reçu du serveur:")
    print(data)'''
    if data == "arret":
        print("Connexion terminé.")
        client_socket.close()

    else:
        while data !="bye":
            message = input("envoi d'un message : ")
            client_socket.send(message.encode())
            print("Message envoyé")
            if message == "arret" or message == "bye":
                print("Connexion terminé.")
                client_socket.close()
                break
            data = client_socket.recv(1024).decode()
            print("Message reçu du serveur:")
            print(data)
            if data == "arret":
                print("Connexion terminé.")
                client_socket.close()
                break
"""

if __name__=="__main__":
    client_socket = socket.socket()
    print("Socket créé.")
    host = "localhost"
    port = input("Choisissez le serveur de connexion : ")

    if port == "1":
        port = 1111
    elif port == "2":
        port = 10000
    else:
        print("Serveur introuvable !")

    client_socket.connect((host, port))
    print("Connecté au serveur.")

    app = QApplication(sys.argv)
    window = client()
    window.show()
    app.exec()
