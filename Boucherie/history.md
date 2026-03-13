

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