file = open('clients.txt', 'r')
lines = file.readlines()
print(lines)
input_name = input("What is your name: ")
print(input_name)
clients_clean = []

for name in lines:
    clients_clean.append(name.strip())

print(lines)
print(clients_clean)
print(input_name)
if input_name in clients_clean:
    print("True")
        