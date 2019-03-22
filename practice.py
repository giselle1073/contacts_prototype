import argparse

parser = argparse.ArgumentParser()
parser.add_argument("command")
args = parser.parse_args()

command = args.command
print(command)

n = {'Giselle': 24, 'Alfredo': 11}

def read_contact_days():
    name = input("What name do you want to get data for?: ")
    print(n[name])




def create_new_contacts():
    name = input("What name do you want to create data for?: ")
    if name in n:
        print("We already have an entry for that name")
        print(n[name])
    else: 
        print('What is your name?: ')
        number = input('How long can you use your contacts for?: ')
        n[name] = number
        print(n[name])
       

def update_new_days():
    name = input("What name do you want to get data for?: ")
    print(n[name])
    numberOfDays = input("What is the number you want to update to?: ")
    n[name] = numberOfDays
    print(n[name])
    
def delete_contacts():
    name = input("What name do you want to delete data for?: ")
    print(n[name])
    if name in n:
        del n[name]


if command == "read":
    print("reading entry...")
    read_contact_days()
elif command == "create":
    print("Creating entry...")
    create_new_contacts()
elif command == "update":
    print("Updating entry...")
    update_new_days()
elif command == "delete":
    print("Deleting entry...")
    delete_contacts()
    print(n)
     
    
          
    
    
    


    

                








	
