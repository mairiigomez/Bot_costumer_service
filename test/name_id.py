####HELL YEAH!
""".py created to verify how to create a dictionary with the file
and then verify witht the dictionary the key and the value
"""
#name = input("What is your name?: ")
#ident =  input("What is yout id?: ")

#file = open('name_id.txt', 'a')
#file.write(name + ' ' + ident + '\n')
#file.close()

#file = open('name_id.txt', 'r')
#info_client = file.readlines()
#file.close()
#clean_info_client = []

#for elements in info_client:
    #clean_info_client.append(elements.strip())
import pprint


dict_clients = {}
with open('name_id.txt') as list_clients:
    for line in list_clients:
        (end_id, name, identification) = line.split(';')
        dict_clients[end_id] = {"name":name,"identification":identification}
print(end_id)
#print(clean_info_client)

pprint.pprint(dict_clients)
name = "Mairiyisel"
ident = "1124413113"
find_client = False
index = 0
for id,user in dict_clients.items():
    index = index +1
    user_db = user.get("name")
    identification_db = user.get("identification").replace('\n','')
    print(user_db, identification_db)
    #print(name)
    if user_db == name and identification_db == ident and index == id:
        print("Eres un cliente")
        find_client = True
if find_client == False:
    db = open("name_id.txt", "a")
    db.write(f'{int(end_id)+1};{name};{ident}\n')    
    db.close()
    print("Would you like to create an account?")
    find_client = True



#for key,value in dict_clients.items():
    #create_account = 0
    #if key == name and value == ident:
     #   print("You are a client")
    

    #name in dict_clients.key  

#if create_account == 1: 
    #print("You are a client")

#else: 
    #print("Would you like to create an account?")