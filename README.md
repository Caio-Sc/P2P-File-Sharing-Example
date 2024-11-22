# P2P File Sharing Example

Este é um exemplo de um sistema básico de compartilhamento de arquivos P2P (peer-to-peer) em Python. O programa permite que peers se conectem entre si para enviar e receber partes de arquivos.

## Funcionalidades

- **Envio de Partes**: Cada peer pode enviar partes de arquivos para outros peers conectados.
- **Recebimento de Partes**: Peers podem salvar partes recebidas de outros peers.
- **Conexão Simultânea**: Implementação multithread para lidar com várias conexões ao mesmo tempo.

## Estrutura do Código

### Classes e Métodos

#### `Peer`
A classe principal que representa um peer no sistema.

- **Atributos**:
  - `ip`: Endereço IP do peer.
  - `port`: Porta na qual o peer escuta conexões.
  - `file_parts`: Lista das partes do arquivo que o peer possui.

- **Métodos**:
  - `listen_for_connections()`: Inicia um servidor para escutar conexões de outros peers.
  - `handle_request(client_socket, peer)`: Processa as solicitações recebidas, salva partes e envia confirmações.
  - `load_part(part_name)`: Carrega uma parte de arquivo do sistema de arquivos.
  - `connect_to_peer(peer_ip, peer_port)`: Conecta-se a outro peer para enviar partes.
  - `save_part(part_name, part_data)`: Salva uma parte de arquivo recebida no sistema de arquivos.

### Fluxo do Programa

1. **Peer 1**:
   - Inicializa um servidor no IP `127.0.0.1` e porta `6881`.
   - Escuta conexões para receber partes.

2. **Peer 2**:
   - Inicializa no IP `127.0.0.1` e porta `6882`.
   - Conecta-se ao Peer 1 e envia partes que possui.

3. **Recebimento**:
   - O Peer 1 salva as partes enviadas pelo Peer 2, caso ainda não as possua.

---

## Como Usar

### Pré-requisitos
- **Python 3.8 ou superior**.
- Bibliotecas padrão do Python (não é necessário instalar bibliotecas externas).

### Passos

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/Caio-Sc/P2P-File-Sharing-Example
   cd P2P-File-Sharing-Example
    ```
2. **Execute os Peers:**:
Execute com python o codigo p2p.py
```bash
python3 p2p.py
```
Você deve ver os arquivos part2.txt_recebida e part3.txt_recebida na pasta raiz do codigo# P2P File Sharing Example

Este é um exemplo de um sistema básico de compartilhamento de arquivos P2P (peer-to-peer) em Python. O programa permite que peers se conectem entre si para enviar e receber partes de arquivos.

## Funcionalidades

- **Envio de Partes**: Cada peer pode enviar partes de arquivos para outros peers conectados.
- **Recebimento de Partes**: Peers podem salvar partes recebidas de outros peers.
- **Conexão Simultânea**: Implementação multithread para lidar com várias conexões ao mesmo tempo.

## Estrutura do Código

### Classes e Métodos

#### `Peer`
A classe principal que representa um peer no sistema.

- **Atributos**:
  - `ip`: Endereço IP do peer.
  - `port`: Porta na qual o peer escuta conexões.
  - `file_parts`: Lista das partes do arquivo que o peer possui.

- **Métodos**:
  - `listen_for_connections()`: Inicia um servidor para escutar conexões de outros peers.
  - `handle_request(client_socket, peer)`: Processa as solicitações recebidas, salva partes e envia confirmações.
  - `load_part(part_name)`: Carrega uma parte de arquivo do sistema de arquivos.
  - `connect_to_peer(peer_ip, peer_port)`: Conecta-se a outro peer para enviar partes.
  - `save_part(part_name, part_data)`: Salva uma parte de arquivo recebida no sistema de arquivos.

### Fluxo do Programa

1. **Peer 1**:
   - Inicializa um servidor no IP `127.0.0.1` e porta `6881`.
   - Escuta conexões para receber partes.

2. **Peer 2**:
   - Inicializa no IP `127.0.0.1` e porta `6882`.
   - Conecta-se ao Peer 1 e envia partes que possui.

3. **Recebimento**:
   - O Peer 1 salva as partes enviadas pelo Peer 2, caso ainda não as possua.

---

## Como Usar

### Pré-requisitos
- **Python 3.8 ou superior**.
- Bibliotecas padrão do Python (não é necessário instalar bibliotecas externas).

### Passos

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/Caio-Sc/P2P-File-Sharing-Example
   cd P2P-File-Sharing-Example
    ```
2. **Execute os Peers:**:
Execute com python o codigo p2p.py
```bash
python3 p2p.py
```
Você deve ver os arquivos part2.txt_recebida e part3.txt_recebida na pasta raiz do codigo