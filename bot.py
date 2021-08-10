"""This is a bot that is going to help to book you next vacation
you can choose any place to the caribbean island 
version: v2
date: 10/08/2021 

We will start with knowing the information of the client
where the client would like to go eventually would like to create 
data bases if the person is not a client yet and go adding little by little"""

import csv

def log_in_client():
    """Ask for credentials of the client verify it a appropiate format"""

    while True:
        name = input("What is your name?: ")
        identification = input("What is your id?: ")

        if str.isdigit(identification) and str.isalpha(name):
            verification(name,identification)
            break
        else:
            print("Please enter a valid data")

def travel_info (name):
    """Ask about the travel information and print a formatted plan trip"""

    print("Let's start building your next vacation!")
    city = input("What is your city of origin?: ")
    destination = input("where would you like to go?: ")
    date = input("What is the best date for your trip?")
    passenger = input("How many people are traveling with you?")
    response = f' ok, {name}, we have booked your trip! \n\
    Departing from {city} going to {destination} in the dates {date} \n\
    and you are traveling with {passenger} people'
    print(response)
    
def verification (name, identification):
    """Know if the client exist in the csv file if not add the client if he/she wants"""
    client_in_file = False
    last_id_client = 0 
    with open('clients_files.csv') as csv_file:
        #read the csv as a dictionary takes the first row as keys
        reader = csv.DictReader(csv_file, delimiter = ";")
        for dict_row in reader: 
            last_id_client += 1
            if dict_row['client'] == name and dict_row['identification'] == identification: 
                client_in_file = True
            
        if client_in_file:
            travel_info(name)

        else: 
            condition = True
            print("would you like to create an account? ")
            print("\n")
            print("1. Yes")
            print("2. No")
            answer = int(input())

            #created the loop in order to ask for a valid option if it was needed
            while condition:
                if answer == 1:
                    with open('clients_files.csv', 'a', newline='') as csv_file:
                        fieldnames = ['number_client', 'client', 'identification'] 
                        writer = csv.DictWriter(csv_file, delimiter=";", fieldnames=fieldnames)
                        writer.writerow({'number_client': last_id_client + 1, 'client':name,'identification':identification})
                    
                    travel_info(name)
                    condition = False  
                
                elif answer == 2:
                    print("ok, thank you for wanted our services")
                    condition == False
                    break

                else:
                    print("Enter a valid option")
                    print("1. yes \n2. no")
                    condition == True
                    answer = int(input())

def main():
    """Main function of the bot to create a vacation"""
    print("""Hi, I am your virtual asistant to help you build your
    next vacation""")
    print("\n")
    log_in_client()
    
if __name__ == '__main__':
    main()