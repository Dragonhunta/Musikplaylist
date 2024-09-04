from random import randint

anzahlSongs = int(input("Gib die Anzahl der Lieder ein: "))
versuche = int(input("Gib die Anzahl der Versuche ein: "))

ergebnisse = []

for i in range(versuche):
    lieder = []
    lieder2 = []

    for i in range(anzahlSongs):
        lieder.append(i)

    print(lieder)
    print()

    while True:
        zahl = randint(0, len(lieder) -1)
        lieder2.append(lieder[zahl])
        # print(lieder2)
        counter = 0
        for j in range(anzahlSongs):
            if j in lieder2:
                counter += 1
        # print(counter)
        # print()
        if counter == anzahlSongs:
            # print(len(lieder2))
            # print()
            ergebnisse.append(len(lieder2))
            break

print(ergebnisse)