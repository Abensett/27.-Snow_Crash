# Défi 10 TocTou **Time-Of-Check to Time-Of-Use**

### Commandes réalisées
```bash
ls -la
cat token
./level10 token
touch /tmp/test
./level10 /tmp/test test
```
### The Outputs
* SUID 

| Terme  | Signification                         | Détails                                                                                              |
|--------|---------------------------------------|------------------------------------------------------------------------------------------------------|
| SUID   | Set User ID                           | - Bit spécial dans les permissions des fichiers.                                                    |
|        |                                       | - Si défini sur un fichier exécutable, le programme s'exécute avec les privilèges du propriétaire.   |
|        |                                       | - Ex. : `passwd` (pour changer les mots de passe, nécessite des privilèges root).                   |
| UID    | User ID                               | - Identifiant unique d'un utilisateur dans le système.                                              |
|        |                                       | - Associé à chaque compte utilisateur dans `/etc/passwd`.                                           |
|        |                                       | - Utilisé pour déterminer les permissions sur des fichiers et ressources.                           |
| GID    | Group ID                              | - Identifiant unique d'un groupe d'utilisateurs.                                                    |
|        |                                       | - Associé à des groupes définis dans `/etc/group`.                                                  |
|        |                                       | - Permet de gérer des permissions partagées pour des utilisateurs appartenant au même groupe.       |

* Connection **via le port 6969**

###  Toctou Exploit
* Ouvrir 3 Terminal avec chaque programme et les lancer un par un
#### tcp_server.py
* créer un serveur tcp qui écoute sur le port 6969
#### toctou.sh 
* alterne les liens symboliques vers le token et un autre fichier avec les droits
#### exec.sh 
* execute le programme en boucle

##### Lancer les 3 programmes avec les deux derniers juste quelques secondes

Password flag09 : woupa2yuojeeaaed06riuj63c
### Answer : feulo4b72j7edeahuete3no7c
