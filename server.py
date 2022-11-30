from socket import *

server = socket(AF_INET, SOCK_STREAM)
server.bind(('localhost', 8086))

server.listen()
users = {("Admin", "password"): "Svitlana Gayduchyk", ("A", "B"): "Name Surname"}
while True:
    user, ip_address = server.accept()
    Login = user.recv(1024)
    Login = Login.decode()
    Passw = user.recv(1024)
    Passw = Passw.decode()
    print(f"Hello, {users[(Login, Passw)]}")
server.close()
