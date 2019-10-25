from math import *

def distanceAcceleration(distance): # distance parcouru lors de l'acceleration 
    distanceParcouruA = 0
    for i in range(10):
        distanceParcouruA += (distance*i) / 60
    return (distanceParcouruA*2) / 1000

def distance2Heures(): # distance parcouru en 2 heures prenant compte de l'acceleration et ralentissement
    distance = (102*90)/60
    distance += distanceAcceleration(10000)
    return distance

def distance1h(distance): # retourne le temps pour moins de 2 heures
    temps = (distance * 60) / 90
    return temps


dico = {("Marseille","Nîmes"): 122, ("Marseille", "Ajaccio"): 521, ("Marseille", "Paris"): 773, ("Marseille","Perpignan"): 317,
        ("Marseille", "Annecy"): 421, ("Marseille", "Besançon"): 564, ("Marseille", "Toulouse"): 403, ("Marseille", "Toulon"): 67,
        ("Nîmes", "Ajaccio"): 605, ("Nîmes", "Paris"): 711, ("Nîmes", "Perpignan"): 203, ("Nîmes", "Annecy"): 359,
        ("Nîmes", "Besançon"): 502, ("Nîmes", "Toulouse"): 290, ("Nîmes", "Toulon"): 190, ("Ajaccio", "Paris"): 1253,
        ("Ajaccio", "Perpignan"): 797, ("Ajaccio", "Annecy"): 901, ("Ajaccio", "Besançon"): 1044, ("Ajaccio", "Toulouse"): 883,
        ("Ajaccio", "Toulon"): 471, ("Paris", "Perpignan"): 846, ("Paris", "Annecy"): 538, ("Paris", "Besançon"): 412,
        ("Paris", "Toulouse"): 676, ("Paris", "Toulon"): 838, ("Perpignan", "Annecy"): 560, ("Perpignan", "Besançon"): 703,
        ("Perpignan", "Toulouse"): 207, ("Perpignan", "Toulon"): 383, ("Annecy", "Besançon"): 215, ("Annecy", "Toulouse"): 646,
        ("Annecy", "Toulon"): 487, ("Besançon", "Toulouse"): 707, ("Besançon", "Toulon"): 627, ("Toulouse", "Toulon"): 468}

##### Variables

distanceAfaire = 0
distanceParcouru2Heures = distance2Heures()
distanceAccKm = distanceAcceleration(10000)
distanceRestant = 0
coef = 0
temps = 0
tempsA = 18
heures = 0
tromper = False

#####

while distanceAfaire == 0: # gere le systeme de choix ville a ville
    if tromper:
        print("Aucune destination trouvé pour ces villes, Veuillez réessayer.")
    villeDeDepart = str(input("Quelle est votre ville de départ ?"))
    villeArrivee = str(input("Quelle est votre ville d'arrivée ?"))
    for cle,distance in dico.items():
        if cle[0] == villeDeDepart and cle[1] == villeArrivee:
            distanceAfaire = distance
            print("La distance a parcourir sera donc de " + str(distanceAfaire) + " km.")
        else:
            tromper = True
        
if (distanceAfaire / distanceParcouru2Heures) > 0 and (distanceAfaire / distanceParcouru2Heures) < 1: # Calcule pour une distance < a 168
    distanceRestant = distanceAfaire - distanceAccKm
    temps = distance1h(distanceRestant) + tempsA
    while temps > 60:
        heures += 1
        temps -= 60
    
#### Gère l'affichage en HH/mm
    if heures < 10:
        if temps < 10:
            print("Temps: 0" + str(heures) +  "/0" + str(ceil(temps)))
        else:
            print("Temps: 0" + str(heures) +  "/" + str(ceil(temps)))
    else:
        if temps < 10:
            print("Temps: " + str(heures) +  "/0" + str(ceil(temps)))
        else:
            print("Temps: " + str(heures) +  "/" + str(ceil(temps)))


else:
    coef = distanceAfaire / distanceParcouru2Heures
    distanceRestant = distanceAfaire % distanceParcouru2Heures
    if distanceRestant < 15:
        temps = distance1h(distanceRestant) + (floor(coef) * 120) + (floor(coef - 1) * 15)
        while temps > 60:
            heures += 1
            temps -= 60
        if heures < 10:
            if temps < 10:
                print("Temps: 0" + str(heures) +  "/0" + str(ceil(temps)))
            else:
                print("Temps: 0" + str(heures) +  "/" + str(ceil(temps)))
        else:
            if temps < 10:
                print("Temps: " + str(heures) +  "/0" + str(ceil(temps)))
            else:
                print("Temps: " + str(heures) +  "/" + str(ceil(temps)))
    else:
        temps = distance1h(distanceRestant) + (floor(coef) * 120) + (floor(coef) * 15)
        while temps > 60:
            heures += 1
            temps -= 60
        if heures < 10:
            if temps < 10:
                print("Temps: 0" + str(heures) +  "/0" + str(ceil(temps)))
            else:
                print("Temps: 0" + str(heures) +  "/" + str(ceil(temps)))
        else:
            if temps < 10:
                print("Temps: " + str(heures) +  "/0" + str(ceil(temps)))
            else:
                print("Temps: " + str(heures) +  "/" + str(ceil(temps)))

    

