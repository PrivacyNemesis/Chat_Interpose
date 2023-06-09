""" SERVEUR """

import socket

HOST_IP = "localhost"
HOST_PORT = 32000
MAX_DATA_SIZE = 1024

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST_IP, HOST_PORT))
s.listen()

print(f"Etablissement d'une connexion sur {HOST_IP}, port {HOST_PORT}...")
connexion_socket, adresse_client = s.accept()
print(f"Connexie établie au client {adresse_client}")

while True:
    message_serveur = input("Vous : ")
    connexion_socket.sendall(message_serveur.encode())

    data_recus = connexion_socket.recv(MAX_DATA_SIZE)
    if not data_recus:
        break
    print("Message : ", data_recus.decode())


s.close
connexion_socket.close()