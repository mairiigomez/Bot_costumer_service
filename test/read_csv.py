import csv


# dict_clients = {}
# with open('clients_files.csv') as file:
#     reader = csv.reader(file, delimiter = ";")
#     for row in reader:
#         #print(f'id :{row[0]}, name: {row[1]}, ident: {row[2]}')
#         number_client, client, ident_client = row[0], row[1], row[2]
#         dict_clients[number_client] = {'name':client, 'identification':ident_client}


dict_clients = {}
with open('clients_files.csv') as file:
    reader = csv.DictReader(file, delimiter = ";")
    # for row in reader:
    #     #print(f'id :{row[0]}, name: {row[1]}, ident: {row[2]}')
    #     number_client = row[number_client]
    #     client = [client]
    #     ident_client = row[ident_client]
        
    #     dict_clients[number_client] = {'name':client, 'identification':ident_client}

    for row in reader:
        print(row['client'])
#print(dict_clients)

# with open('clients_files.csv', 'a', newline='') as f:
#     fieldnames = ['number_client', 'client', 'identification']
#     writer = csv.DictWriter(f, delimiter=";", fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerow({'number_client':'10', 'client':'Felix','identification':'1233332'})

with open('clients_files.csv', 'a', newline='') as f:
    fieldnames = ['number_client', 'client', 'identification']
    writer = csv.DictWriter(f, delimiter=";", fieldnames=fieldnames)
    #writer.writeheader()
    writer.writerow({'number_client':'10', 'client':'Felix','identification':'1233332'})


