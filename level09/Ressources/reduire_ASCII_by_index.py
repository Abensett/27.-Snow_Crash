import sys  # Importation du module sys pour acceder aux arguments de la ligne de commande
# Recuperation de l'argument passed en ligne de commande (le hash)
chaine_hachee = sys.argv[1]
# Initialisation d'une variable pour stocker le resultat final
message_original = ""
# Parcours de chaque caractere dans la chaine hachee
for indice in range(0, len(chaine_hachee)):
    # Pour chaque caractere, on modifie son code ASCII en fonction de sa position (indice)
    # On ajoute le caractere modifie a la chaine 'message_original'
    message_original = message_original + chr(ord(chaine_hachee[indice]) - indice)
# Affichage du message decode
print(message_original)
