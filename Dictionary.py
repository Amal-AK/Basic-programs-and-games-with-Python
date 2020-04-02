import  urllib.request , urllib.parse, urllib.error
import json

# Structures  ------------------------------------------------------------------------------------------------------------
langues = {
    1: "en" ,
    2: 'fr' ,
    3:'ar' ,
    4: 'es' ,
    5:'ru' ,
    6:'de' ,
    7:'it' ,
    8:'ko',
    9:'tr' ,

}

parms = dict() # paramétres de l url

exit = 'y'

# inputs -----------------------------------------------------------------------------------------------------------------------

while (exit == 'y') :
    try:
        x = int( input("Enter the number of Language :  \n 1- English \n 2- French \n 3- Arabic \n 4- Spanish \n 5- Russian \n 6- German \n 7- Italian \n 8- Korean \n 9- Turkish \n The number :  "))
    except :
        print( "Error , enter an integer")
        quit()
    try :
        parms['lang'] =langues[x]
    except :
        print("Enter the correct number !")
        quit()

    word = input("\n Enter the word to define :   ")
    try :
        parms['define'] = word
    except :
        print("Enter a word !")
        quit()

# get the data form google API -----------------------------------------------------------------------------------------------------------------

    serviceurl = 'https://googledictionaryapi.eu-gb.mybluemix.net/?'
    url = serviceurl + urllib.parse.urlencode(parms)
    print("======================= WE ARE SEARCHING ============================ ")
    data = urllib.request.urlopen(url)
    try:
        js = json.loads(data.read())
    except:
        js = None

    if not js :
        print('==== Failure To Retrieve the word ====')
        continue

# printing the result -----------------------------------------------------------------------------------------------------------------------------


    print("Word : ", js[0]["word"])
    print("Word : ", js[0]["meaning"])
    exit = input("Enter 'y' to roll again : ")
