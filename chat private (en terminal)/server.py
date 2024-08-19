import socket

def start_server(host='0.0.0.0', port=65432):
    # Crée un socket TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Associe le socket à l'adresse et au port
        server_socket.bind((host, port))
        # Écoute les connexions entrantes
        server_socket.listen()
        print(f"Serveur en attente de connexion sur {host}:{port}")

        # Accepte la connexion
        conn, addr = server_socket.accept()
        with conn:
            print(f"Connecté à {addr}")
            while True:
                # Reçoit des données du client
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Client: {data.decode()}")
                # Envoie des données au client
                response = input("Vous: ")
                conn.sendall(response.encode())

if __name__ == "__main__":
    start_server()
