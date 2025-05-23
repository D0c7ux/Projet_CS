﻿#  Journalisation des fenêtres actives - Python

Ce projet permet de **suivre les fenêtres actives** sur un ordinateur Windows, en enregistrant **le nom de chaque application utilisée** ainsi que **le temps passé dessus**, dans un fichier de log (enetre.log).

>  Projet éducatif à but légal, utile pour mesurer sa productivité ou apprendre la journalisation système en Python.

---

##  Fonctionnalités

-  Surveillance continue des fenêtres actives
-  Calcul automatique du **temps passé** sur chaque fenêtre
-  Enregistrement dans un fichier enetre.log
-  Lecture des logs via une interface web en local (log.php)
-  Messages en français pour une meilleure accessibilité

---

##  Comment ça marche ?

1. **Fonction get_window_title()** (à coder) récupère le titre de la fenêtre active.
2. Chaque 5 secondes :
   - Le script détecte si le titre a changé.
   - Sil y a changement :
     - Il calcule combien de temps la fenêtre précédente est restée active.
     - Il écrit une ligne dans enetre.log contenant :
       `
       [date et heure] Fenetre active : <nom> (temps: hh:mm:ss)
       `
3. Le fichier log est ensuite **consultable en ligne** via un serveur Apache local et une page log.php.

---

