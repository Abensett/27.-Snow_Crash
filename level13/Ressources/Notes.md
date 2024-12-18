# Défi 13  binary / strings / gdb / disas / breakpoints
### Commandes réalisées
```bash
./level13
strings level13
gdb -q ./level13 # Quiet Mode
disas main       # display code assembleur de `main` -> comprendre ce que fait exactement cette fonction
b *main+14       # `main` is a function pointer, and you want to set a breakpoint at a specific offset from the beginning of the function pointed to by `main` = un point d'arrêt 14 octets après le début de la fonction `main`
r              # Run
print $eax     # Afficher la valeur du registre **`eax`**
set $eax=4242  # Modifie pour la valeur attendu
cont
```
#### CMD strings
* utilisée pour extraire des séquences de caractères lisibles à partir d'un fichier binaire
#### disas
* This can be useful for understanding how the program is executing at a low level.
### Breakpoint
| Aspect | Breakpoint |
| ---- | ---- |
| **Définition** | Point dans le code où l'exécution du programme est interrompue. |
| **Utilité** | Permet aux développeurs d'inspecter l'état du programme pendant le débogage. |
| **Exemple (avec GDB)** | Commande `break` ou `b` suivi de l'emplacement du point dans le code. |
**`cmp $0x1092,%eax`** : Il s'agit d'une **instruction de comparaison (`cmp`)**.
- **`$0x1092`** : La valeur immédiate à comparer (ici, **`0x1092`**, en hexadécimal, équivaut à 4242 en décimal).
- **`%eax`** : Le registre **`eax`** est utilisé comme opérande pour la comparaison. C'est un registre général dans l'architecture x86, et il contient la valeur retournée par la fonction **`getuid`**