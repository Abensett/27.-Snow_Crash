import socket  # Import du module socket

PORT = 6969  # Port d'écoute
HOST = '0.0.0.0'  # Écoute sur toutes les interfaces

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Création du socket TCP
    s.bind((HOST, PORT))  # Liaison à l'adresse et au port
    s.listen(1)  # Écoute d'une connexion

    while True:
        conn, addr = s.accept()  # Accepte la connexion d'un client
        print('Connected by', addr)  # Affiche l'adresse du client
        
        while True:
            data = conn.recv(1024)  # Reçoit des données
            if not data:  # Si aucune donnée, déconnecte
                break
            print(data)  # Affiche les données reçues

# Exécution uniquement si le script est lancé directement
if __name__ == '__main__':
    main()  # Démarre le serveur
