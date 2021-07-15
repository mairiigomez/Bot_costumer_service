""" 
This is a bot that is going to help to book you next vacation
you can choose any place to the caribbean island 
version: v1
date: 14/07/2021 

We will start with knowinng the information of the client
where the client would like to go eventually would like to create 
data bases if the person is not a client yet and go adding little by little 

"""
clients = ["Jose" , "Maira" , "Mairiyisel" , "Daniela" , "Angeles"]
print("Buenos dias soy su asistente virtual")
print("Por favor regala tus datos para ayudater en tu siguiente aventura")
print("\n")
name = input("Perfecto,como es tu nombre? : ")
if name in clients:
    city = input("En que ciudad te encuentras? : ")
    id_ = input("Como es numero de identificación? : ")
    print("\n")
    print("Ok!!, ahora regalame los datos de tu viaje")
    print("\n")
    origin = input("Desde cual ciudad seria tu punto de partida? :")
    destination = input("A cual ciudad te diriges? :")
    date = input("Fecha de aventura? :")
    quota = input("Cuantas personas van? :")
    
    response = f'Ok,{name}, tu viaje fue programdo con exito!! \n\
         Tu vuelo partirá desde la ciudad de {origin} con \n\
         destino a la ciudad {destination} en la fecha {date}\n\
         y tienes tiques para {quota} personas'

    
    print(response)
else: 
    print("would you like to create an account? ")
    print("\n")
    print("1. Yes")
    print("2. No")
    answer = int(input())
    if answer == 1:
        clients.append([name])
        print(*clients, sep = "\n")
    
    elif answer == 2:
        print("ok, thank you for wanted our services")
    
    else:
        print("Enter a valid option")