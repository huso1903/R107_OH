jour = int(input("entrer le jour du mois (jour):" ))
heure = int(input("entrer l'heure (de 0 à 23) " ))
minute = int (input("entrer la minute (de 0 à 59) " ))  
minutes_écoulées = (jour - 1) * 24 * 60 + heure * 60 + minute
print (f"le nombre de minute écoulées depuis le début du mois est : {minutes_écoulées} minutes.")
