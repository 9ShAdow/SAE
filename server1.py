import socket
import  os 
import psutil
import platform
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


#host devra changer avec un ficher CSV 

server_socket = socket.socket()
print("Socket crée.")
host = "localhost"
port = 1111
server_socket.bind((host, port))
print("Socket sur l'adresse {} et le port {}".format(host, port))
server_socket.listen(1)
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
str_2 = psutil.cpu_percent()

print("En attente du client")
conn, address = server_socket.accept()
print("Conexion établie avec le client {}".format(address))




mem_usage = psutil.virtual_memory()



data = conn.recv(1024).decode()
data = data.lower()

# DIFFERENTES FONCTIONS 

def ram():
    str_1 = mem_usage.percent
    str_2 = mem_usage.total/(1024**3)
    
    #str_2 = psutil.cpu_percent(4)
    #conn = str("CPU % used:", psutil.cpu_percent())
    #server_socket.send(rep.encode())
    
    #print('The CPU usage is: ', psutil.cpu_percent(4), '%')
    rep = str(f"La RAM Libre est: {str_1} % \nLa RAM Utilisé est: {str_2}")
    conn.send(rep.encode())
    
 
    
    
    #print(f"RAM Totale: {mem_usage.total/(1024**3):.2f}G")
    #print(f"RAM Libre: {mem_usage.percent}%")
    #print(f"RAM Utilisé: {mem_usage.used/(1024**3):.2f}G")
    #print('RAM memory % used:', psutil.virtual_memory()[2])
    # Getting usage of virtual_memory in GB ( 4th field)
    #print('RAM Used (GB):', psutil.virtual_memory()[3]/1000000000)
def cpu():
    str_1 = psutil.cpu_percent()
    str_2 = psutil.cpu_percent(4)
    #conn = str("CPU % used:", psutil.cpu_percent())
    #server_socket.send(rep.encode())
    
    #print('The CPU usage is: ', psutil.cpu_percent(4), '%')
    rep = str(f" The CPU used is: {str_1} \n The CPU usage is: {str_2} %")
    conn.send(rep.encode())
    #
    # 
    # print(rep)
    


    #server_socket.send(rep.encode())
def osn():
    print('OS:', platform.system(), "version", platform.release())
    #server_socket.send(data.encode())
def ip():
    #rep= str("L'addresse IP de la machine est :", IPAddr)
    print("L'addresse IP de la machine est :", IPAddr)
    #server_socket.send(rep.encode())
def name():
    print('Le nom de la machine est :', platform.node())
    '''on peut aussi faire hostname = socket.gethostname()
        print("Your Computer Name is:" + hostname)'''
def dir():
# Using listdir() function.
    listOfFileNames = os.listdir()
    # Print the name of all files in the current working directory.
    print("Following is the list of names of all the files present in the current working directory: ")
    print(listOfFileNames)



while data !="arret":
    #conn.recv(1024).decode()
    #data = conn.recv(1024).decode()
    #data = data.lower()
    #reply = ("saisir un message: ")
    #conn.send(reply.encode())

    reply = ("saisir un message: ")
    conn.send(reply.encode())
    print("Réponse envoyé")
    data = conn.recv(1024).decode()
    print(f"Message {data} reçue du client:")


    data = data.lower()
    

    if data == "arret":
        print("Connexion terminé")
        conn.close()
    elif data == "ram":
        print("RAM")
        ram()
        pass
    elif data == "cpu":
        print("CPU")
        cpu()
        pass
    elif data == "os":
        osn()
    elif data == "ip":
        ip()
    elif data == "name":
        name()
    elif data =="dos:dir":
        dir()
    elif data.startswith("dos:") and platform.system() == "Windows":
        #split apres : 
        #partie apres : va dans vartiable 
        cmd = data.split(":")
        os.system(cmd[1])
        conn.send.data(cmd)

    elif data.startswith("Linux:") and platform.system() == "Linux":
        cmd = data.split(":")
        os.system(cmd[1])
        print("ok")
    else:
        print("La commande n'existe pas cliquer sur l'aide ou taper --help pour pour voir l'ensemble des commandes possibles")
        #faire un truc qui change la couleur du texte de aide dans la IG du client
        pass

    reply = ("le message a bien été reçu")
    conn.send(reply.encode())

print(f"Message {data} reçue du client:")
print("Réponse envoyé")
    #data = conn.recv(1024).decode()
    
    
   

print("Connexion terminé.")
conn.close()