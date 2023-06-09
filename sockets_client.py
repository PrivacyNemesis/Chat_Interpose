""" CLIENT """

import socket
import time

HOST_IP = "localhost"
HOST_PORT = 32000
MAX_DATA_SIZE = 1024

print(f"Etablissement d'une connexion au serveur {HOST_IP}, port {HOST_PORT}...")

while True:
    try:
        s = socket.socket()
        s.connect((HOST_IP, HOST_PORT))
    except:    
        print(f"La connexion au serveur {HOST_IP} a echouer. Nouvelle tentative...")
        time.sleep(10)
    else:
        print(f"Connecté au serveur {HOST_IP}")
        break


while True:
    data_recus = s.recv(MAX_DATA_SIZE)
    if not data_recus:
        break 
    print("Message : ", data_recus.decode())
    message_serveur = input("Vous : ")
    s.sendall(message_serveur.encode())

s.close()    