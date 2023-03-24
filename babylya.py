import random
counter_bye = 0

print("ЧЕГО СКАЗАТЬ-ТО ХОТЕЛ, МИЛОК?!")
while True:
    rand =  random.randint(1930, 1950)
    if counter_bye == 3:
        print("ДО СВИДАНИЯ, МИЛЫЙ!")
        break
    else:
        s = input()
        if s == "ПОКА!": 
            counter_bye+=1
            print("НЕТ, НИ РАЗУ С",rand, "ГОДА!")
            continue
        elif str.isupper(s):
            print("НЕТ, НИ РАЗУ С", rand, "ГОДА!")
        else:
            print("АСЬ?! ГОВОРИ ГРОМЧЕ, ВНУЧЕК!")