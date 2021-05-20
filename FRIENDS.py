JoeyList = ["Rynata", "Amro", "Wejdan", "Abduallah", "Menna", "Neslihan", ]

RachelList = ["Nouran", "Nadine", "Wejdan", "Abduallah", "Deniz", "Rand"]

RossList = ["Rynata", "Amro", "Wejdan", "Abduallah", "Hassan", "Rand"]

ChandlerList = ["Nadine", "Dilan", "Nada", "Nouran", "Hassan", "Rand"]

PhoebeList = ["Rynata", "Amro", "Dilan", "Nadine", "Hassan", "Rand"]

MonicaList = ["Rynata", "Amro", "Wejdan", "Abduallah", "Hassan", "Rand"]

FriendsList = ['Rachel', 'Ross', 'Monica', 'Chandler', 'Joey', 'Phoebe']

allList = JoeyList + RossList + ChandlerList + RachelList + PhoebeList + MonicaList + FriendsList


def CatchDublicates(allList):
    lastList = []
    for d in allList:
        if d not in lastList:
            lastList.append(d)
    return lastList


print("The friends that are invited to the party are:")
print(CatchDublicates(allList))
