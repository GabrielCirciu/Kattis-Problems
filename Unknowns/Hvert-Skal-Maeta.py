cities_dict = {
    "Reykjavik": [0, 388], "Kopavogur": [6, 387], "Hafnarfjordur": [12, 391], "Reykjanesbaer": [48, 427],
    "Akureyri": [388, 0], "Gardabaer": [9, 389], "Mosfellsbaer": [16, 371], "Arborg": [64, 428],
    "Akranes": [49, 350], "Fjardabyggd": [659, 290], "Mulathing": [603, 216], "Seltjarnarnes": [4, 390]
}

location = input()
if cities_dict[location][0] < cities_dict[location][1]:
    print("Reykjavik")
else:
    print("Akureyri")