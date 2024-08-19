import socket

def start_client(server_ip, server_port):
    # Crée un socket TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        # Connecte le socket au serveur
        client_socket.connect((server_ip, server_port))
        print(f"Connecté au serveur {server_ip}:{server_port}")

        while True:
            # Envoie des données au serveur
            message = input("Vous: ")
            client_socket.sendall(message.encode())
            # Reçoit des données du serveur
            data = client_socket.recv(1024)
            print(f"Serveur: {data.decode()}")

if __name__ == "__main__":
    # Remplacez 'localhost' par l'adresse IP du serveur si nécessaire
    start_client('localhost', 65432)
