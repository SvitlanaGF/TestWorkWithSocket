from socket import *

client = socket(AF_INET, SOCK_STREAM)
client.connect(('localhost', 8086))
Login = input("Login: ")
client.send(Login.encode())
Passw = input("Password: ")
client.send(Passw.encode())
client.close()
