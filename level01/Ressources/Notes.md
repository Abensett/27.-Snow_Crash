## Défi 1 BRUTE FORCE

### Mise en place de la connexion ssh / scp avec virtualbox
* [[Utiliser ssh scp with Ubuntu on Virtuallbox]]
### Commandes réalisées

```bash
cd ..
chmod 777 level00 # Pour pouvoir transférer via scp
cat /etc/passwd | grep flag01 > pswdflag01 # je stocke le mdp et le récupère dans ma machine physique avec SCP
```
### passwd file UNIX
## Why ?
### Stores session info
| Composant                  | Description                                            |
| -------------------------- | ------------------------------------------------------ |
| **Fichier /etc/passwd**    | Stocke les informations des comptes utilisateurs.      |
| **Format de ligne**        | Chaque ligne représente un utilisateur avec des champs tels que nom d'utilisateur, UID, GID, etc. |
| **Champs clés**            | Nom d'utilisateur, UID (identifiant utilisateur), GID (identifiant de groupe), Répertoire de démarrage, Shell par défaut. |
## How ?

### Format
`username:password:UID:GID:GECOS:home_directory:login_shell`

## Example ?

| Nom d'utilisateur | Mot de passe | UID  | GID  | Informations générales | Répertoire de démarrage | Shell par défaut |
| ----------------- | ------------ | ---- | ---- | ---------------------- | ----------------------- | ---------------- |
| alice             | x            | 1001 | 1001 | Alice Doe              | /home/alice             | /bin/bash        |
**Un caractère x indique que le mot de passe est chiffré est stocké dans [le fichier /etc/shadow](https://www.malekal.com/quest-ce-que-etc-shadow-et-son-role/).**

#### Output : 42hDRfypTqqnw

#### Outil John the Ripper 
.\john.exe –show passwordfile


### Answer : abcdefg