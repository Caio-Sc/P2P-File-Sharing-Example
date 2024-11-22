import socket
import threading
import os
import time

class Peer:
    def __init__(self, ip, port, file_parts):
        self.ip = ip
        self.port = port
        self.file_parts = file_parts  # Lista de partes do arquivo que este peer possui

    def listen_for_connections(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.ip, self.port))
        server_socket.listen(5)
        print(f"Listening on {self.ip}:{self.port}")
        while True:
            client_socket, addr = server_socket.accept()
            threading.Thread(target=self.handle_request, args=(client_socket, self)).start()  # Passando 'self' para a thread

    def handle_request(self, client_socket, peer):
        part_data = client_socket.recv(1024).decode()  # Receber dados da parte
        part_name, part_content = part_data.split(":", 1)
        
        # Salvar parte, se necessário
        if part_name not in peer.file_parts:
            peer.save_part(part_name, part_content.encode())
            print(f"Parte {part_name} salva.")
        
        # Enviar confirmação de recebimento (ACK)
        client_socket.send(f"Parte {part_name} recebida com sucesso.".encode())
        client_socket.close()



    def load_part(self, part_name):
        with open(part_name, 'r') as f:
            return f"{part_name}:{f.read()}".encode()

    def connect_to_peer(self, peer_ip, peer_port):
        for part in self.file_parts:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((peer_ip, peer_port))  # Abre uma nova conexão para cada parte
            part_data = self.load_part(part)
            client_socket.send(part_data)  # Envia uma parte
            ack = client_socket.recv(1024).decode()  # Aguarda o ACK
            print(f"ACK recebido para {part}: {ack}")
            client_socket.close()  # Fecha a conexão




    def save_part(self, part_name, part_data):
        with open(part_name + "_recebida", 'wb') as f:
            f.write(part_data)

if __name__ == "__main__":
    # Exemplo de uso
    peer1 = Peer('127.0.0.1', 6881, ['part1', 'part2'])
    threading.Thread(target=peer1.listen_for_connections).start()

    # Atrasar a conexão do peer2 para garantir que o peer1 está pronto
    time.sleep(1)  # Espera 1 segundo

    peer2 = Peer('127.0.0.1', 6882, ['part2.txt', 'part3.txt'])
    peer2.connect_to_peer('127.0.0.1', 6881)  # Peer 2 se conecta ao Peer 1
