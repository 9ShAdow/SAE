import socket
import  os 
import psutil
import platform
from PyQt6.QtWidgets import *
from PyQt6.QtCore import * 
import sys
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

        ram= QPushButton("ram")
        cpu=QPushButton("cpu")

        grid.addWidget(ram, 0, 0)
        grid.addWidget(cpu , 1, 0)

        ram.clicked.connect(self.__actionram)
        cpu.clicked.connect(self.__actioncpu)


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
