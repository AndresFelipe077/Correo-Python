import smtplib, ssl
import getpass

username = input("Ingresa tu nombre de usuario: ")
#password = getpass.getpass("Ingresa tu password: ")
password = input("Ingresa tu password: ")

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as server:
    server.login(username,password)
    print("Iniciaste sesión! ")
    destinario = input("Ingrese el destinatario: ")
    mensaje = input("Ingresa el mensaje: ")
    for i in range(15):#43
        server.sendmail(username, destinario, mensaje)
    print("Mensaje enviado")