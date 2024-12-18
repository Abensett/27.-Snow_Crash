import sys  # Importation du module sys pour accéder aux arguments de la ligne de commande
# Récupération de l'argument passé en ligne de commande (le hash)
chaine_hachée = sys.argv[1]
# Initialisation d'une variable pour stocker le résultat final
message_original = ""
# Parcours de chaque caractère dans la chaîne hachée
for indice in range(0, len(chaine_hachée)):
    # Pour chaque caractère, on modifie son code ASCII en fonction de sa position (indice)
    # On ajoute le caractère modifié à la chaîne 'message_original'
    message_original = message_original + chr(ord(chaine_hachée[indice]) - indice)
# Affichage du message décodé
print(message_original)