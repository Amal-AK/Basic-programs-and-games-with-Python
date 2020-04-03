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
        print(" => the word you want to search : " , js[0]["word"] , "\n")
        for k ,v in (js[0]["meaning"]).items() :
            print('\n   ', k)
            for k1 , v1 in v[0].items() :
                print("\t\t-",k1 , ': ',v1 )
        print("\n")
# if we use french , because the struct is diff
    if (x==2) :
            print(" => Le mot recherché  : ", js[0]["word"])
            for k ,v in js[0]["meaning"].items() :
                print("\t" ,k , ": définitions\n")
                for k1 , v1 in v.items() :
                    for item in v1 :
                        for k2 , v2 in item.items() :
                            if (len(v2)!=0 and v2[0]!= '') : print("\t  -", k2 ,':', v2)
                        if (len(item['definition'])!= 0) : print('\n')

    exit = input("  Enter 'y' to roll again : ")
