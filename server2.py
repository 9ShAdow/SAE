import socket

import sys

import psutil #pip install psutil # https://pypi.org/project/psutil/ # https://psutil.readthedocs.io/en/latest/ 
import platform #pip install platform # https://pypi.org/project/platform/ # https://docs.python.org/3/library/platform.html
import socket #pip install socket # https://pypi.org/project/socket/ # https://docs.python.org/3/library/socket.html
#import netifaces #pip install netifaces # https://pypi.org/project/netifaces/ # https://netifaces.readthedocs.io/en/latest/
import netaddr #pip install netaddr # https://pypi.org/project/netaddr/ # https://netaddr.readthedocs.io/en/latest/
import os
import socket

def serveur():
    msg = ""
    conn = None
    server_socket = None
    host = socket.gethostname()
    ram = psutil.virtual_memory() 
    ram1 = ram[0]/1000000000
    ram2 = ram[1]/1000000000
    ram3 = ram[3]/1000000000
    #IPAddr = socket.gethostbyname(host)


    stockage = psutil.disk_usage("/")
    stockage1 = stockage[0]/1000000000
    stockage2 = stockage[1]/1000000000
    stockage3 = stockage[2]/1000000000

    cpu = psutil.cpu_count()
    name = socket.gethostname()
    ip = socket.gethostbyname(name)
    while msg != "kill" :
        msg = ""
        server_socket = socket.socket()
        """ options qui permette de réutiliser l'adresse et le port rapidement"""
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        server_socket.bind(("localhost", 15001))

        server_socket.listen(1)
        print('Serveur en attente de connexion')
        while msg != "kill" and msg != "reset":
            msg = ""
            try :
                conn, addr = server_socket.accept()
                print (addr)
            except ConnectionError:
                print ("erreur de connection")
                break
            else :
                while msg != "kill" and msg != "reset" and msg != "disconnect":
                    msg = conn.recv(1024).decode()
                    print ("Received from client: ", msg)
                    # msg = input('Enter a message to send: ')
                    if data == "ram":
                            reply = str(f"\nRAM Total: {round(ram1, 2)} GB \nRAM Disponible: {round(ram2,2)} GB \nRAM Utilisée : {round(ram3,2)} GB")  
                            conn.send(reply.encode())
                            print("Message ram envoyé")
                            data = conn.recv(1024).decode()
                            print(f"Message reçu : {data}")

   
                    elif data == "dercommande":
                        ficher = open("historique.txt", "r")
                        with open ("historique.txt", "r") as ficher:
                            derniere_ligne = ficher.readlines()[-2]
                            print(derniere_ligne)
                        reply = derniere_ligne
                        conn.send(reply.encode())
                        print("Message dercommande envoyé")
                        data = conn.recv(1024).decode()
                        print(f"Message reçu : {data}")

                    elif data.startswith("dos:"):
                        try:
                            if platform.system() == "Windows":
                                win = data.split(":")
                                cmd = win[1]
                                reply = os.popen(cmd[1]).read()
                                conn.send(reply.encode())
                                print(f"Message ", cmd ," envoyé")
                            else:
                                reply = "La commande DOS n'est pas disponible sur votre système d'exploitation"
                                conn.send(reply.encode())
                        except:
                            reply = "La commande DOS n'est pas disponible sur votre système d'exploitation"
                        #conn.send(reply.encode())

                    elif data.startswith("Linux:"):
                        try:
                            if platform.system() == "Linux":
                                lin = data.split(":")
                                cmd = lin[1]
                                #reply = os.system(cmd)
                                reply = os.popen(cmd[1]).read()
                                conn.send(reply.encode())
                                print(f"Message ", cmd ," envoyé")
                            else:
                                reply = "La commande Linux n'est pas disponible sur votre système d'exploitation"
                                conn.send(reply.encode())
                        except:
                            reply = "La commande Linux n'est pas disponible sur votre système d'exploitation"
                            conn.send(reply.encode())
                    
                    elif data.startswith("PowerShell:"):
                        try:
                            if platform.system() == "Windows":
                                win = data.split(":")
                                cmd = win[1]
                                #reply = os.system(cmd)
                                reply = os.popen(cmd[1]).read()
                                conn.send(reply.encode())
                                print(f"Message ", cmd ," envoyé")
                            else:
                                reply = "La commande PowerShell n'est pas disponible sur votre système d'exploitation"
                                conn.send(reply.encode())
                        except:
                            reply = "La commande PowerShell n'est pas disponible sur votre système d'exploitation"
                            conn.send(reply.encode())

                    elif data == "cpu":
                        str_1 = psutil.cpu_percent()
                        str_2 = psutil.cpu_percent(4)
                        reply = str(f" The CPU used is: {str_1} \n The CPU usage is: {str_2} %")
                        conn.send(reply.encode())
                        print("Message cpu envoyé")
                        data = conn.recv(1024).decode()
                        print(f"Message reçu :  {data} ")


                    elif data == "name":
                        reply = str(f"Le nom de la machine est : {name} \n ")
                        conn.send(reply.encode())
                        print("Message name envoyé")
                        data = conn.recv(1024).decode()
                        print(f"Message reçu : {data}")

    
                    elif data == "ip":
                        reply = (f"L'addresse IP de la machine est : {ip} \n ") 
                        conn.send(reply.encode())
                        print("Message ip envoyé")
                        data = conn.recv(1024).decode()
                        print(f"Message reçu : {data}")

                    elif data == "help":
                            reply = ("Commande disponible:\n \n - La commande ram permet d'afficher la ram totale, la ram utilisée et la ram libre \n - La commande ip permet d'afficher l'adresse ip de la machine \n  - La commande os permet d'afficher le nom et la version de l'os \n - La commande name permet d'afficher le nom de la machine \n - La commande port permet d'afficher le port utilisé \n - La commande cpu permet d'afficher le nombre de coeur de la machine \n - La commande disque permet d'afficher le stockage total, le stockage utilisé et le stockage libre") 
                            conn.send(reply.encode())
                            print("Message help envoyé")
                            data = conn.recv(1024).decode()
                            print(f"Message reçu : {data}")
                    elif data == "os":
                        str_1 = platform.system()   
                        str_2 = platform.release()
                        reply = str(f" OS : {str_1} \n Version : {str_2}")
                        conn.send(reply.encode())
                        print("Message os envoyé")
                        data = conn.recv(1024).decode()
                        print(f"Message reçu : {data}")

                    elif data == "--help":
                        reply = ("Commande disponible:\n \n - La commande ram permet d'afficher la ram totale, la ram utilisée et la ram libre \n - La commande ip permet d'afficher l'adresse ip de la machine \n  - La commande os permet d'afficher le nom et la version de l'os \n - La commande name permet d'afficher le nom de la machine \n - La commande port permet d'afficher le port utilisé \n - La commande cpu permet d'afficher le nombre de coeur de la machine \n - La commande disque permet d'afficher le stockage total, le stockage utilisé et le stockage libre") 
                        conn.send(reply.encode())
                        print("Message help envoyé")
                        data = conn.recv(1024).decode()
                        print(f"Message reçu : {data}")
                    elif data == "python --version":
                        reply = sys.version
                        conn.send(reply.encode())
                        print("Message python --version envoyé")
                        data = conn.recv(1024).decode()
                        print(f"Message reçu : {data}")

                    elif data == "ls -la":
                        reply = os.popen(data).read()
                        conn.send(reply.encode())
                        print("Message ls -la envoyé")
                        data = conn.recv(1024).decode()
                        print(f"Message reçu : {data}")

                    elif data == "get-process":
                        try:
                            if platform.system() == "PowerShell":
                                reply = os.popen(data).read()
                                conn.send(reply.encode())
                                print("Message get-process envoyé")
                                data = conn.recv(1024).decode()
                                print(f"Message reçu : {data}")
                            else:
                                reply = "Commande non disponible"
                                conn.send(reply.encode())
                                print("Message get-process envoyé")
                                data = conn.recv(1024).decode()
                                print(f"Message reçu : {data}")
                        except:
                            print("Erreur de saisie")
                            conn.send(data.encode())
                            print("Message help envoyé")
                            data = conn.recv(1024).decode()
                            print(f"Message reçu : {data}")


                    elif data.startswith("ping"):
                            if platform.system() == "Windows":
                                try:
                                    pong = data.split()[1] 
                                    print (pong)
                                    reply = os.system("ping -n 1 " + pong)
                                    if reply == 0:
                                        reply = os.popen(data).read()
                                        print("Le ping a fonctionné")
                                        conn.send(reply.encode())
                                        print("Message help envoyé")

                                    else:
                                        reply = "Network Error"
                                        print("Le ping n'a pas fonctionné")
                                        conn.send(reply.encode())
                                        print("Message help envoyé")
                                        data = conn.recv(1024).decode()
                                        print(f"Message reçu : {data}")

                                except:
                                    print("Erreur de saisie")
                                    conn.send(data.encode())
                                    print("Message help envoyé")
                                    data = conn.recv(1024).decode()
                                    print(f"Message reçu : {data}")

                                    #fichier = open('historique.txt', 'w')
                                    #fichier.write(data + "\n")
                                    #print("fait")
                                    #fichier.close()

                                if platform.system() == "Linux" or platform.system() == "Darwin":
                                    try:
                                        pong = data.split()[1] 
                                        print (pong)
                                        reply = os.system("ping -c 1 " + pong)
                                        if reply == 0:
                                            reply = os.popen(data).read()
                                            print("Le ping a fonctionné")
                                            conn.send(reply.encode())
                                            print("Message help envoyé")
                                            data = conn.recv(1024).decode()
                                            print(f"Message reçu : {data}")
                                            
                                        else:
                                            reply = "Network Error"
                                            print("Le ping n'a pas fonctionné")
                                            conn.send(reply.encode())
                                            print("Message help envoyé")
                                            data = conn.recv(1024).decode()
                                            print(f"Message reçu : {data}")

                                    except:
                                        print("Erreur de saisie")
                                        data = conn.recv(1024).decode()
                                        print(f"Message reçu : {data}")

                                        #fichier = open('historique.txt', 'w')
                                        #fichier.write(data + "\n")
                                        #print("fait")
                                        #fichier.close()
                                else:
                                    print("Message help envoyé")
                                    data = conn.recv(1024).decode()
                                    print(f"Message reçu : {data}")

                                    #fichier = open('historique.txt', 'w')
                                    #fichier.write(data + "\n")
                                    #print("fait")
                                    #fichier.close()
                else:  
                    #split apres :
                    #verification 
                
                    verif = os.system(data)
                    cmd = os.popen(data).read()

            # = 0 on a un resultat 
                    if verif == 0:
                        for i in range (1):
                            print("la commande est valide")
                            conn.send(cmd.encode())
                            data = conn.recv(1024).decode()
                            print(f"Message reçu : {data}")
                            #repver = "la commande a bien été executé"
                            #conn.send(repver.encode())s
                        
                    

                    else:
                        if cmd == "":
                                cmd = "la commande n'existe pas "
                                conn.send(cmd.encode())
                                print("Message help envoyé")
                                data = conn.recv(1024).decode()
                                print(f"Message reçu : {data}")
                        else:
                            try:
                                conn.send(cmd.encode())
                                print("Message help envoyé")
                                data = conn.recv(1024).decode()
                                print(f"Message reçu : {data}")

                            except:
                                cmd = "erreur d'envoi"
                                conn.send(cmd.encode()) 
                                print("Message help envoyé")
                                data = conn.recv(1024).decode()
                                print(f"Message reçu : {data}")



                    conn.send(msg.encode())
                conn.close()
        print ("Connection closed")
        server_socket.close()
        print ("Server closed")