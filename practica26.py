import socket


def iniciar_cliente():
    # 1. Crear el socket TCP del cliente
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = '127.0.0.1'
    puerto = 8080

    print(f"[*] Intentando conectar con el servidor en {host}:{puerto} (Iniciando TCP Handshake: SYN)...")

    # 2. Conectar al servidor (Envía SYN -> Recibe SYN-ACK -> Envía ACK)
    try:
        cliente_socket.connect((host, puerto))
    except Exception:
        print("ERROR!")
        raise

    print("[+] ¡Conexión TCP establecida con el servidor!")

    # 3. Simular una petición HTTP de la World Wide Web
    peticion_http = "GET / HTTP/1.1\r\nHost: localhost\r\nConnection: close\r\n\r\n"
    print("[+] Enviando solicitud HTTP a través del canal TCP seguro...")
    cliente_socket.send(peticion_http.encode('utf-8'))

    # 4. Recibir la respuesta del servidor
    respuesta = cliente_socket.recv(4096).decode('utf-8')
    print(f"\n--- Respuesta recibida del servidor ---\n{respuesta}")

    # 5. Cerrar el socket
    cliente_socket.close()
    print("[*] Cliente desconectado.")


if __name__ == "__main__":
    iniciar_cliente()
