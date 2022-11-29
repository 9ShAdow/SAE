import socket
import  os 
import psutil
import platform


server_socket = socket.socket()
print("Socket crée.")
host = "localhost"
port = 1111
server_socket.bind((host, port))
print("Socket sur l'adresse {} et le port {}".format(host, port))
server_socket.listen(1)
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

print("En attente du client")
conn, address = server_socket.accept()
print("Conexion établie avec le client {}".format(address))

data = conn.recv(1024).decode()
print("Message", data,"received from the client:")


 

def ram():
    print('RAM memory % used:', psutil.virtual_memory()[2])
    # Getting usage of virtual_memory in GB ( 4th field)
    print('RAM Used (GB):', psutil.virtual_memory()[3]/1000000000)
def cpu():
    print('CPU % used:', psutil.cpu_percent())
    print('The CPU usage is: ', psutil.cpu_percent(4), '%')
def os():
    print('OS:', platform.system(), "version", platform.release())
def ip():
    print("L'addresse IP de la machine est :", IPAddr)
def name():
    print('Le nom de la machine est :', platform.node())
    '''on peut aussi faire hostname = socket.gethostname()
        print("Your Computer Name is:" + hostname)'''


while data !="arret":
    reply = ("saisir un message: ")
    conn.send(reply.encode())
    print("Réponse envoyé")
    data = conn.recv(1024).decode()
    print(f"Message {data} reçue du client:")
    if data == "arret":
        print("Connexion terminé")
        conn.close()
    elif data == "ram":
        ram()
    elif data == "cpu":
        cpu()
    elif data == "os":
        os()
    elif data == "ip":
        ip()
    elif data == "name":
        name()
    else:
        print("La commande n'existe pas cliquer sur l'aider ou taper --help pour pour voir l'ensemble des commandes possibles")
        #faire un truc qui change la couleur du texte de aide dans la IG du client
        pass



print("Connexion terminé.")
conn.close()