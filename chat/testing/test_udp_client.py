import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(b'Test message', ('localhost', 8080))#отправляет сообщение(байт строку)