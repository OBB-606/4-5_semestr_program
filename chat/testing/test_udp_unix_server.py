#Рассмотрим тип сокета (UNIX socket), который не использует ip и порт в качестве точки обмена, в качестве нее будет использоваться
#какой-то файл. Т.е. в рамках одного компьютера не надо резервировать порт.
#Точка обмена - файл, который создается в папке самой программы, например.
#!!!!!!!!!ДЛЯ UNIX-ПОДОБНЫХ СИСТЕМ!!!!!!!!!!!!!!!!
import os
import socket


unix_sock_name = 'unix.sock'
sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

if os.path.exists(unix_sock_name):#проверка: создавался ли этот файл ранее, были ли попытки работать с этим
#UNIX socket'ом до запуска сервера. Если такой файл уже существует, то мы его удаляем
    os.remove(unix_sock_name)
sock.bind(unix_sock_name)#происходит резервирование этого файла

while True:
    try:
        result = sock.recv(1024)
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        print("Message: ", result.decode("utf-8"))