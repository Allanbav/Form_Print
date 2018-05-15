import os

def Skull():
    os.system('cls')
    # Manually set characters on screen for funs
    print(("x"*11)+("\n")+("x"*11))
    print(("x"*3)+(" "*5)+("x"*3)+("\n")+("x"*3)+(" "*5)+("x"*3))
    print(("x"*3)+(" ")+("x")+(" ")+("x")+(" ")+("x"*3))
    print(("x"*3)+(" ")+("x")+(" ")+("x")+(" ")+("x"*3))
    print(("x"*3)+(" "*5)+("x"*3))
    print(("x"*4)+(" ")+("x")+(" ")+("x"*4))
    print(("x"*5)+(" ")+("x"*5))
    print(("x"*11) + ("\n") + ("x"*11) + "\n")


def character_check(Ffirst):
    # checking name for alpha characters, ask for a valid response if function returns false. Rechecks name again
    while 'True':
        if Ffirst.isalpha():
            return Ffirst
        else:
            Ffirst = input("Please enter a valid name \n")
            continue

def chooseAccount():
    # hardcoded list, second list will hold needed accounts for text output
    accountHold = ['HOTSOS', 'V1', 'Universal Desktop', 'EMAIL', 'NEWTORK', 'Infogenesis', 'Ericom', 'Delphi']
    accountActive = []
    
    #Loop through the accounts asking if they are needed
    for i in accountHold:
        Skull()
        print("Do you need "+i+"?")
        answer = input("y or n?\n")
        #when response is a single lowercase 'y'- i, which is the current account, is added to empty list.
        if answer =='y':
            accountActive.append(i)
            os.system('cls')

        else:
            os.system('cls')
    return accountActive

def printout(first, last, account):
    

    if account == "HOTSOS":
        print(account +"\n")
        print("USER: " +first[0][0]+last.lower()+"jh")
        print("PASS: " +last.capitalize()+"1530 \n")
    elif account == "EMAIL":
        print(account +"\n")
        print("USER: " +first[0][0]+last.lower()+"thejouledallas.com")
        print("PASS: " +last.capitalize()+"1530 \n")
    elif account == "V1":
        print(account +"\n")
        print("USER: " +first[0][0]+last.lower())
        print("PASS: " +"*LEAVE BLANK*\n")
    elif account == "Universal Desktop":
        print(account +"\n")
        print("USER: " +first+"."+last)
        print("PASS: \n")
    elif account == "Infogenesis":
        print(account +"\n")
        print("ID: \n")
    #elif account == "Delphi":
        #print(account +"\n")
        #altlast = " ".join(ord(char) -96 for char in last)
        #print("USER: " +first[0][0]+last.lower())
        #print("PASS: ".join(altlast)+"\n")
    else:
        print(account +"\n")
        print("USER: " +first[0][0]+last.lower())
        print("PASS: " +last.capitalize()+"1530 \n")

def count_printout(i, first, last, active):
    while i <len(active):
        printout(first,last,active[i])
        i += 1

def main():
    while 1:
        Skull()
        first = input("First Name: ")
        first = character_check(first)
        Skull()
        last = input("Last Name: ")
        last = character_check(last)
        active= chooseAccount()
        Skull()
        i = 0
        count_printout(i, first, last, active)
        os.system('pause')
        #while i <len(active):

            #printout(first, last, active[i])
           # i += 1
    else:
        print("1 is no longer True, Something went wrong. ")

main()
