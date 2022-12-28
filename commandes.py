import socket
from server1 import *
# Importing the library
import psutil
import os



def rep(data):
    if data == "ram":
        ram()
    elif data == "cpu":
        cpu()
    elif data == "os":
        osn()
    elif data == "ip":
        ip()
    elif data == "name":
        name()
    elif data == "dir":
        dir()
    elif data == "exit":
        exit()
    else:
        print("Commande introuvable")

def ram():
    str_1 = mem_usage.percent
    str_2 = mem_usage.total/(1024**3)
    
    #str_2 = psutil.cpu_percent(4)
    #conn = str("CPU % used:", psutil.cpu_percent())
    #server_socket.send(rep.encode())
    
    #print('The CPU usage is: ', psutil.cpu_percent(4), '%')
    rep = str(f"La RAM Libre est: {str_1} % \nLa RAM Utilisé est: {str_2}")
    
    conn.send(rep.encode())
    
 
    
    
    
def cpu():
    str_1 = psutil.cpu_percent()
    str_2 = psutil.cpu_percent(4)
    #conn = str("CPU % used:", psutil.cpu_percent())
    #server_socket.send(rep.encode())
    
   
    rep = str(f" The CPU used is: {str_1} \n The CPU usage is: {str_2} %")
    conn.send(rep.encode())
    

   
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
'''tt dans le cmd split pour tout 
def dir():
# Using listdir() function.
    listOfFileNames = os.listdir()
    # Print the name of all files in the current working directory.
    print("Following is the list of names of all the files present in the current working directory: ")
    print(listOfFileNames)'''

#temps que on ne recoit pas le mot arret on continue a recevoir des données

#peut être faire directement les fonctions dans le while a voir 








    #break
#print("Réponse envoyé")
#data = conn.recv(1024).decode()
#print(f"Message {data} reçue du client:")   #reply = ("le message a bien été reçu")
#conn.send(reply.encode())

print(f"Message {data} reçue du client:")
print("Réponse envoyé")
    #data = conn.recv(1024).decode()
    
    
   

print("Connexion terminé.") 
conn.close()
def port():
    port = input("Choisissez le serveur de connexion : ")

    if port == "1":
        port = 1111
    elif port == "2":
        port = 10000
    else:
        print("Serveur introuvable")
