

### Je veux implémenter une fonctionnalité qui utilise la géolocalisation pour trouver la boucherie la plus proche. Le module doit calculer la distance entre l'utilisateur et une liste de coordonnées de boucheries nantaises (commence par 'LA SOBREDA' à Bouguenais) et renvoyer la plus proche en moins de 2 secondes.
Voici la User Story (US) et ses Critères d'Acceptation (AC) pour la fonctionnalité demandée :

```markdown
**User Story : Trouver la boucherie la plus proche**

**En tant que** client pressé,
**Je souhaite** trouver rapidement la boucherie la plus proche de ma position actuelle,
**Afin de** gagner du temps et de faciliter mes achats en me dirigeant vers l'établissement le plus accessible.

---

**Critères d'Acceptation :**

1.  **Calcul de la distance :** Le module doit calculer la distance géographique (à vol d'oiseau) entre la position actuelle de l'utilisateur (latitude, longitude) et les coordonnées de chaque boucherie de la liste fournie.
2.  **Source des données des boucheries :** Le module doit utiliser une liste prédéfinie de coordonnées de boucheries nantaises pour le calcul. Cette liste doit inclure, à titre d'exemple et de test, la boucherie 'LA SOBREDA' à Bouguenais.
3.  **Identification de la plus proche :** Le module doit identifier sans équivoque la boucherie dont la distance calculée est la plus courte par rapport à la position de l'utilisateur.
4.  **Retour du résultat :** Le module doit renvoyer les informations clés (nom, adresse, coordonnées) de la boucherie identifiée comme étant la plus proche.
5.  **Performance :** L'intégralité du processus, depuis la réception de la position de l'utilisateur jusqu'au retour de la boucherie la plus proche, doit s'exécuter en moins de 2 secondes.
6.  **Gestion de l'indisponibilité de la géolocalisation :** Si la position de l'utilisateur ne peut être obtenue (ex: géolocalisation désactivée ou erreur), le système doit informer l'utilisateur de l'impossibilité de réaliser la recherche et l'inviter à activer sa géolocalisation.
7.  **Gestion de l'absence de boucherie :** Si la liste des boucheries est vide ou si aucune boucherie n'est trouvable (selon des critères futurs si applicables, ou simplement "dans la liste"), le système doit l'indiquer clairement à l'utilisateur.
```

### Feature: Maintenant que la base fonctionne, je veux que tu modifies trouver_boucherie.py pour qu'il ne cherche pas seulement LA SOBREDA, mais qu'il compare avec 5 autres boucheries de Loire-Atlantique (Rezé, Nantes centre, etc.) et qu'il me donne la meilleure option en fonction du trafic estimé.
Voici l'User Story que je te propose, avec ses critères d'acceptation pour guider le développement :

```markdown
## User Story: Comparaison Multiboucheries avec Optimisation Trafic

**En tant que** client cherchant de la viande de qualité en Loire-Atlantique,
**Je veux** obtenir une comparaison des temps de trajet pour plusieurs boucheries de mon choix (dont LA SOBREDA),
**Afin de** sélectionner rapidement la meilleure option en fonction du trafic estimé et d'optimiser mon parcours.

---

### Critères d'Acceptation :

*   **AC1 : Liste de Boucheries Configurable**
    *   Le système doit permettre de spécifier une liste d'au moins 6 boucheries en Loire-Atlantique à comparer (ex: La Sobreda, une boucherie à Rezé, une à Nantes centre, une à St-Herblain, une à Carquefou, une à Bouguenais). Cette liste doit être facilement configurable (via un fichier de configuration ou une structure de données dédiée).
*   **AC2 : Calcul du Temps de Trajet par Boucherie**
    *   Pour chaque boucherie de la liste spécifiée, le système doit calculer le temps de trajet estimé depuis un point de départ donné (par défaut ou configurable par l'utilisateur).
*   **AC3 : Prise en Compte du Trafic**
    *   Le calcul du temps de trajet doit impérativement intégrer les données de trafic en temps réel ou estimé pour fournir une information pertinente.
*   **AC4 : Identification de la Meilleure Option**
    *   Le système doit clairement identifier et présenter la boucherie offrant le temps de trajet le plus court comme étant la "meilleure option".
*   **AC5 : Affichage des Résultats Comparatifs**
    *   Les résultats doivent être présentés de manière structurée, affichant pour chaque boucherie son nom, son adresse et son temps de trajet estimé.
*   **AC6 : Localisation du Code**
    *   Les modifications et la nouvelle logique de comparaison doivent être implémentées dans le fichier `trouver_boucherie.py`.
*   **AC7 : Gestion des Erreurs**
    *   Le système doit gérer et informer l'utilisateur si une boucherie est introuvable ou si les données de trafic ne peuvent pas être obtenues pour une destination spécifique.
```