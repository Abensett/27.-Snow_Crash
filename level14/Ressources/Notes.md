## Défi 14 [[ltrace vs ptrace]]

### Commandes réalisées

#### Bash

```bash
ltrace getflag
cat /etc/passwd | grep flag14 # 3014 pour flag14
gdb -q getflag
```

#### gdb

```gdb
disas main
catch syscall ptrace # how it inracts with the system
commands 1
> set ($eax) = 0
> continue
> end
b getuid
r
s
print $eax
set $eax=3014
s
```

### Reversing

> Méthode modifier eax = 0 pour dire que ptrace ne block pas et modifier eax = 3014 lors du uid pour trouver le flag14

1.  désassemblage de la fonction `main`
2.  breakpoint pour l'appel système `ptrace`
3.  **liste de commandes à exécuter** lorsque le breakpoint est atteint
4.  initialise la valeur du registre `eax` à 0 (eax est souvent utilisé pour les valeurs de retours des appels system), puis continue jusqu'au breakpoint suivant
5.  breakpoint pour l'appel système `getuid`
6.  Modification de eax pour avoir l'id du flag14

### Outputs

### Answer : 7QiHafiNa3HVozsaXkawuYrTstxbpABHD8CPnHJ

## More info :

### ltrace vs ptrace

| Aspect                     | ltrace                                                                                                                                                                    | ptrace                                                                                                           |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **Définition**             | Outil de **traçage des appels de fonctions** d'un programme.                                                                                                              | Système d'API du noyau Linux pour **contrôler et déboguer les processus**.                                       |
| **Utilisation Principale** | Enregistre et affiche les appels de fonctions et les bibliothèques partagées utilisées par un programme.                                                                  | Permet au processus parent de suivre, inspecter et modifier l'exécution d'un processus enfant.                   |
| **Fonctionnalités Clés**   | Affichage des appels de fonctions, des arguments et des valeurs de retour, permettant de comprendre le comportement du programme du point de vue des appels de fonctions. | Attachement à un processus, suivi des appels système, inspection et modification des registres et de la mémoire. |

Un programme peut appeler ptrace avec l’option PTRACE_TRACEME. Voici ce qui se passe dans ce cas :

Le processus demande à être tracé par un parent.
Si un débogueur est déjà attaché au processus, l’appel à ptrace(PTRACE_TRACEME, ...) échoue et retourne une erreur.

- Bypass ptrace : https://gist.github.com/poxyran/71a993d292eee10e95b4ff87066ea8f2
