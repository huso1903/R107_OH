minute_ecoulees = int(input("entrer le nombre de minute écoulées depuis le début du mois "))
jour = minute_ecoulees //(24*60) + 1
reste_minute = minute_ecoulees %(24*60)
heure = reste_minute//60
minute = reste_minute % 60
print(f"la date associée est {jour} jour {heure} heure {minute} minute " )


