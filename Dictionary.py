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
    print("\n============================================ WE ARE SEARCHING ====================================================\n ")
    try :
        data = urllib.request.urlopen(url)
    except :
        print("Error, check if the word is corect or exist , then check if you are connected to internet ")
        quit()
    try:
        js = json.loads(data.read())
    except:
        js = None

    if not js :
        print('==== Failure To Retrieve the word ====')
        continue

# printing the result -----------------------------------------------------------------------------------------------------------------------------

# if we use english
    if (x==1) :
        print("Word serched  : ", js[0]["word"])
        tab1 = list(js[0]["meaning"])
        for l in tab1 :
            print("\n",l , ": \n")
            tab2 = list(js[0]["meaning"][l][0])
            for z in tab2 :
                print("   - " ,z , " : " , js[0]["meaning"][l][0][z])

# if we use french , because the struct is diff
    if (x==2) :
            print("Le mot recherché  : ", js[0]["word"])
            tab1 = list(js[0]["meaning"])
            for l in tab1 :
                print("\n",l , ":  Définitions" )
                tab2 = list(js[0]["meaning"][l]["definitions"])
                for w in tab2 :
                    if (len(w["definition"])!= 0 ) : print("\n")
                    tab3= list(w)
                    for t in tab3 :
                        if (len(w[t]) != 0) :
                            print("   - " , t , " : " , w[t])
    exit = input("\n Enter 'y' to roll again : ")
