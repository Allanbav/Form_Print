import os


def Skull():
    os.system('cls')
    # Manually set characters on screen for funs
    print("""




                                                                                                      ..
                                                                                                      ..
                                                                                                      ..
                                                                                                      ..
                                                                                                      ..
                                                                                                      ..
                                                                                                      .,
                                                                                                      .,
                                                                                                      ,,
                                  ,,,.                                                                ,,
                                 ./#(,                                                                ,,
                                 ./#/.                                                                ,,
                                  *(/.                                                                ,*
                                  *(*                                                                 ,*
                                  ,/,                                                                 **
                                  .*,                                                                 **
                                  .,.                                                                 **
                                   .                                                                  **
                                                                                                      **
                                                                                                      **
                                                                                                      */
                                                                                                      //.
                                                                                                     .//.
                                                                                                     .//.
                                                                                                     .//.
                                                                                                     .//.
                                                                                                     .//.
                                                                                                     .//.
                                                    ..,,...                                          ./(.              ...,,,..
                                 ./#(,          ,/(#%%%#%%%#(*.         ./#/.              ,(#*      .((.           .*(#%%##%%%(/,
                                 ,(%(,       ./%(*.         ./##*.      .(%(.              ,#%/      .((.        ,(%#/,        .*(%#*.
                                 ,(%(,      ,#%,              .#%(,     .(%(.              ,#%/      .((.      ./%#/.             *#%/.
                                 ,(%(,     *#%(                ,(%(,    .(%(.              ,#%/      .((.      /%#*                ,#%/
                                 ,(%(,    ,(%(,                 *#%/.   .(%(.              ,#%/      .((,      #%/.                 *##
                                 ,(%(,    *%%*                  ./%#,   .(%(.              ,#%/      ,((,     .%%%##################%%%.
                                 ,(%(,    *%%*                  ./%#,   .(%(.              ,#%/      ,((,     .%#/,,,,,,,,,,,,,,,,,,,,,
                                 ,(%(,    ,#%/.                 ,(%(.   .(%(,              ,#%/      ,((,     .%#*
                                 ,(%(,    ./%#*                ./%#*    ./%#*              *%#*      ,##,      #%(.
                                 ,(%(,      ,#%,              .#%(,      ./%#*           .*#%/.      ,##,      ./%%/.              .,,
                                 ,(%(,       ./%(*.         .*##*.        ./%%/        .,(%#*.       ,##,        ,(%#/,         .,/#%(.
                                 ,(%(,         *(%%#(/***/(#%#(.            ,/##(/////(%%#/.         ,##,          ,/#%#(/****/#%%#/,
                                 ,(%(,           .,*/(((((/*,.                 */(((((/,.            .**.             .//((((((*,.
                                 ,(%(,
                                 ,(%(,
                                 ,(%(,
                                 ,(%(,
                                 ,(%(,
                                 ,(%(,
                                 ,(%(,
                                 ,(#(,
                                 ,(#(.
                                 ,(#/.
                                 *##/.
                                 *##*.
                                ./##*
                                ./#(,
                                ,(#/.
                                ,(#*
                               ./#(.
                               .(#*
                               ,((,
                               /(*.
                               (/.
                              .(,
                              **
                             ,/.
                            ,/,
                           ,*,
                          .*,
                         .,.
                       ...
                       .
                             """)
    #print(("█"*11)+("\n")+("█"*11))
    #print(("█"*3)+(" "*5)+("█"*3)+("\n")+("█"*3)+(" "*5)+("█"*3))
    #print(("█"*3)+(" ")+("█")+(" ")+("█")+(" ")+("█"*3))
    #print(("█"*3)+(" ")+("█")+(" ")+("█")+(" ")+("█"*3))
    #print(("█"*3)+(" "*5)+("█"*3))
    #print(("█"*4)+(" ")+("█")+(" ")+("█"*4))
    #print(("█"*5)+(" ")+("█"*5))
    #print(("█"*11) + ("\n") + ("█"*11) + "\n")


def character_check(Ffirst):
    # checking name for alpha characters, ask for a valid response if function returns false. Rechecks name again
    while 'True':
        if Ffirst.isalpha():
            return Ffirst
        else:
            Ffirst = input("Please enter a valid name \n")
            continue

def hotelProperty():
    y = 1
    while y ==1:
        hotel = input("Is this a Lumen - ""L"" or Joule - ""J"" Account?\n")
        if hotel in ("L", "l", "Lumen", "lumen"):
            return "lumen"
        elif hotel in ("J", "j", "Joule", "joule"):
            return "joule"
        else:
            print("Invalid response")
            continue

def chooseAccount():
    # hardcoded list, second list will hold needed accounts for te█t output
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

def printout(first, last, account, property,tpass):

    if account == "HOTSOS":
        print(account +"\n")
        print("USER: " +first[0][0]+last.lower()+"jh")
        print("PASS: " +last.capitalize()+tpass+" \n")
    elif account == "EMAIL":
        print(account +"\n")
        print("USER: " +first[0][0]+last.lower()+"@the" + property + "dallas.com")
        print("PASS: " +last.capitalize()+tpass+" \n")
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
        print("PASS: " +last.capitalize()+tpass+" \n")

def count_printout(i, first, last, active,property,tpass):
    while i <len(active):
        printout(first,last,active[i],property,tpass)
        i += 1

def main():
    while 1:
        Skull()
        first = input("First Name: ")
        first = character_check(first)
        Skull()
        last = input("Last Name: ")
        last = character_check(last)
        property = hotelProperty()
        tpass = "hold"
        if property == "lumen":
            tpass = "6101"
        else:
            tpass = "1530"
        active= chooseAccount()
        Skull()
        i = 0
        count_printout(i, first, last, active,property,tpass)
        os.system('pause')
        #while i <len(active):

            #printout(first, last, active[i])
           # i += 1
    else:
        print("1 is no longer True, Something went wrong. ")

main()




