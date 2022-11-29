import socket
from server1 import *
# Importing the library
import psutil
import os



def port():
    port = input("Choisissez le serveur de connexion : ")

    if port == "1":
        port = 1111
    elif port == "2":
        port = 10000
    else:
        print("Serveur introuvable")
