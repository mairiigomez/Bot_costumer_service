""" 
This is a bot that is going to help to book you next vacation
you can choose any place to the caribbean island 
version: v1
date: 14/07/2021 

We will start with knowinng the information of the client
where the client would like to go eventually would like to create 
data bases if the person is not a client yet and go adding little by little 

"""
#make the variable condition global so I can use it
#in both function with no problem ps: this method did not work
#I had to break the code in the while function



#function to know the details about the trip
#have to send the parameter to the function 
def travel_info (name):
    print("Let's start building your next vacation")
    city = input("What is your city of origin?")
    destination = input("where would you like to go?")
    date = input("What is the best date for your trip?")
    passenger = input("How many people are traveling with you?")
    response = f' ok, {name}, we have booked your trip! \n\
    Departing from {city} going to {destination} in the dates {date} \n\
    and you are traveling with {passenger} people'
    print(response)
    
#know if the client exist in the data base if not add 
#it if he/she wants
def verification (name):
    db = open("clients.txt", "r")
    clients = db.readlines()
    clients_clean = []

    for name_db in clients:
        clients_clean.append(name_db.strip())

    #print(clients)
    #print(clients_clean)
    #clients = clients.split(" ")
    #print(clients)
    

    if name in clients_clean:
        #print("True")
        travel_info(name)    

    else: 
        condition = True
        print("would you like to create an account? ")
        print("\n")
        print("1. Yes")
        print("2. No")
        answer = int(input())

        #created the loop in order to ask for a valid option if it was needed
        while condition == True:
            if answer == 1:
                db = open("clients.txt", "a")
                #this way it give an enter after each name separate them
                db.write(name + "\n")    
                #db = open("clients.txt", "r")
                #print_list = db.read()
                db.close()
                travel_info(name)
                condition = False

                #broke the code because I was not able to take it out of the loop
                #break     
            
            elif answer == 2:
            
                print("ok, thank you for wanted our services")
                condition == False

                break

            else:
                print("Enter a valid option")
                print("1. yes \n  2. no")
                condition == True
                answer = int(input())

def main():
    print("Hi, I am your virtual asistant")
    print("Your virtual vacation")
    print("""May I please have your information to help you to 
    create your next aventure""")
    print("\n")
    #db = open("clients.txt", "r")
    #clients = db.read()
    name = input("What is your name: ")

    verification(name)

if __name__ == '__main__':
    main()