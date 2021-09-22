def watTheFuckDoeJeMetJeLeven():
    vraag = input('wat is je naam en je leeftijd?\n')
    if vraag == 'stop': 
        print(vraag)
        print('finished')
    else: 
        print(vraag)
        watTheFuckDoeJeMetJeLeven()

watTheFuckDoeJeMetJeLeven()