import socket

#on va faire un ficher pour lancer tt les serveurs en meme temps ensuite en fonction des num on pourra choisir le serveur

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


if message == "arret" or message == "bye":
    print("Connexion terminé.")
    client_socket.close()
else:
    data = client_socket.recv(1024).decode()
    print("Message reçu du serveur:")
    print(data)
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
