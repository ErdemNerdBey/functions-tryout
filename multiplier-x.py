def tafel(antwoord):
    for i in range(11):
        print(i * antwoord)

antwoord = input('kies een getal waar je de tafel van wil weten')
tafel(int(antwoord))