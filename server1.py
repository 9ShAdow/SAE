import sys
from PyQt6.QtWidgets import QApplication, QWidget #pip install PyQt6
import psutil #pip install psutil # https://pypi.org/project/psutil/ # https://psutil.readthedocs.io/en/latest/ 
import platform #pip install platform # https://pypi.org/project/platform/ # https://docs.python.org/3/library/platform.html
import socket #pip install socket # https://pypi.org/project/socket/ # https://docs.python.org/3/library/socket.html
#import netifaces #pip install netifaces # https://pypi.org/project/netifaces/ # https://netifaces.readthedocs.io/en/latest/
import netaddr #pip install netaddr # https://pypi.org/project/netaddr/ # https://netaddr.readthedocs.io/en/latest/
import os
import socket



host = socket.gethostname()
ram = psutil.virtual_memory() 
ram1 = ram[0]/1000000000
ram2 = ram[1]/1000000000
ram3 = ram[3]/1000000000
'''ping = os.system("ping -c 1 " + host)
if ping == 0:
    pingstatus = "Network Active"
    print("Le ping a fonctionné")
else:
    pingstatus = "Network Error"
    print("Le ping n'a pas fonctionné")
'''
stockage = psutil.disk_usage("/")
stockage1 = stockage[0]/1000000000
stockage2 = stockage[1]/1000000000
stockage3 = stockage[2]/1000000000

cpu = psutil.cpu_count()
name = socket.gethostname()
ip = socket.gethostbyname(name)

ip = socket.gethostbyname(host)
#adresse_ip = netifaces.ifaddresses('en0')[2][0]['addr'] # en0 = ethernet,si votre adresse ip est sur une autre interface il faudra changer "en0" par le nom de l'interface
#netaddr_adresse_ip = netaddr.IPAddress(adresse_ip)


host = "localhost" # "", "127.0.0.1
port = 7000

server_socket = socket.socket()
server_socket.bind((host, port))
server_socket.listen(1)

print('En attente du client')
conn, address = server_socket.accept()
print(f'Client connecté {address}')

print("Socket sur l'adresse {} et le port {}".format(host, port))
data = conn.recv(1024).decode()
 
while data != "kill":
    if data == "kill" or data == "kill":
        break

    elif data == "ram":
        reply = str(f"\nRAM Total: {round(ram1, 2)} GB \nRAM Disponible: {round(ram2,2)} GB \nRAM Utilisée : {round(ram3,2)} GB")  
        conn.send(reply.encode())
        print("Message ram envoyé")
        data = conn.recv(1024).decode()
        print(f"Message reçu : {data}")

   

    elif data == "cpu":
        str_1 = psutil.cpu_percent()
        str_2 = psutil.cpu_percent(4)
        reply = str(f" The CPU used is: {str_1} \n The CPU usage is: {str_2} %")
        conn.send(reply.encode())
        print("Message cpu envoyé")
        data = conn.recv(1024).decode()
        print(f"Message reçu :  {data} ")


    elif data == "name":
        reply = str(name)
        conn.send(reply.encode())
        print("Message name envoyé")
        data = conn.recv(1024).decode()
        print(f"Message reçu : {data}")

    
    elif data == "ip":
        #reply = str(netaddr_adresse_ip)
        conn.send(reply.encode())
        print("Message ip envoyé")
        data = conn.recv(1024).decode()
        print(f"Message reçu : {data}")


    elif data == "os":
        str_1 = platform.system()   
        str_2 = platform.release()
        reply = str(f"System: {str_1} \nRelease: {str_2}")
        conn.send(reply.encode())
        print("Message os envoyé")
        data = conn.recv(1024).decode()
        print(f"Message reçu : {data}")

    elif data == "port":
        reply = str(port)
        conn.send(reply.encode())
        print("Message port envoyé")
        data = conn.recv(1024).decode()
        print(f"Message reçu : {data}")
    
    elif data == "stockage":
        reply = str(f"Espace total: {round(stockage1, 2)} GB \nEspace  Disponible: {round(stockage2,2)} GB \nEspace libre : {round(stockage3,2)} GB")
        conn.send(reply.encode())
        print("Message disque envoyé")
        data = conn.recv(1024).decode()
        print(f"Message reçu : {data}")

    elif data =="ping":
        reply = os.system("ping -c 4 " + host)
        if reply == 0:
            pingstatus = "Network Active"
            print("Le ping a fonctionné")
        else:
            pingstatus = "Network Error"
            print("Le ping n'a pas fonctionné")

    else:
        message = input("Message au client ->")
        print("Message envoyé")
        conn.send(message.encode())
        data = conn.recv(1024).decode()
        print(f"Message du client :{message}")
    



# Fermeture
conn.close()
print("Fermeture de la socket client")
server_socket.close()
print("Fermeture de la socket serveur")