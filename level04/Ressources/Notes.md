## Défi 4 Manipulation de l'URL via HTTP + Exploit = Injection de commande

### Commandes réalisées
```bash
ls -la
cat level04.pl
nc localhost 4747
curl localhost:4747?x=\`getflag\`
```
* localhost:4747
### 1.  Fichier perl :
* être exécuté en tant que script CGI (Common Gateway Interface) sur un serveur web. Il semble prendre un paramètre "x" à partir de la requête CGI, exécute une fonction x qui utilise le paramètre pour exécuter une commande shell, puis renvoie le résultat au navigateur.
* en-tête HTTP pour indiquer que le contenu qui suit est de type texte/html.
*  **`sub x { ... }` :** Cela indique que vous définissez une sous-routine nommée `x`. Les accolades `{ ... }` délimitent le corps de la sous-routine.
    
- **`$y = $_[0];` :** Cela initialise une variable `$y` avec la première valeur  donné en argument

- `print echo $y 2>&1`: Cela utilise la fonction `print` pour afficher le résultat de la commande shell `echo $y 2>&1` = sortie standard. = **sortie de getflag**

Le serveur attend une requête GET avec un paramètre `x`. Ce paramètre est récupéré et exécuté comme une commande shell dans le script Perl. Par exemple, une requête comme `curl localhost:4747?x=\`getflag``fera exécuter la commande`getflag` sur le serveur, permettant d'obtenir un flag. Cette situation représente une **vulnérabilité d'injection de commande**.
### 2. Use netcat pour test connection : Oui si du texte peut être entré
### 3. ``?x=\`getflag\`` est la partie de l'URL qui spécifie le paramètre`x`avec la valeur de la commande système`getflag`.