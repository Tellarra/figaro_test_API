# figaro_test_API
# :house: Test technique FCMS

## :blue_book: Le projet

Le but de ce mini projet est d'écrire une API permettant de :
- Créer une alerte immobilière
- Lister les alertes immobilières d'un utilisateur

### Le domaine

Une alerte immobilière est constituée des informations suivantes :

| Champ | Obligatoire |
|---|---|
| Un identifiant  | Oui  |
| L'identifiant de l'utilisateur créant l'alerte  | Oui  |
| Une date de création  | Oui  |
| Le nom de l'alerte  | Oui  |
| Un prix minimum | Non  |
| Un prix maximum  | Non  |
| Une ville  | Oui  |

## Pour tester l'API
### Création d'une alerte
Dans POSTMAN il faut créer un nouvel environnement avec l'adresse url suivante : https://figaro-test-api.herokuapp.com

Il suffit ensuite de tester dans body pour l'action POST /alerts :

    {
    "name_alert" : "Maison 1",
    "city" : "Paris",
    "price_min" : 300000.0,
    "price_max" : 400000.0,
    "account_id" : 1
    }

    {
    "name_alert" : "Maison 2",
    "city" : "Melbourne",
    "price_min" : 600000.0,
    "price_max" : 700000.0,
    "account_id" : 2
    }

### Lister les alertes
Tester dans body pour l'action GET /alerts, il suffit de clicker sur SEND pour envoyer la requête et avoir la liste des alertes associées à un compte utilisateur.

### Tester l'API
Pour tester un peu plus l'API, vous pouvez essayer dans POST alerts :

    {
        "name_alert" : "Maison 3",
        "city" : 3,
        "price_min" : 300000.0,
        "price_max" : 400000.0,
        "username" : "Marie1"
    }

    --> Cela va retourner un message d'erreur pour la ville.

    {
        "name_alert" : "Maison 3",
        "city" : "Melbourne",
        "price_min" : 500000.0,
        "price_max" : 300000.0,
        "username" : "Marie1"
    }

    --> Cela va retourner un message d'erreur pour le prix minimum qui est plus grand que le maximum.

    {
        "name_alert" : "Maison 3",
        "city" : "Melbourne",
        "price_min" : null,
        "price_max" : null,
        "username" : "Marie1"
    }

    --> Cela ne va pas retourner d'erreur.

    Si le 'username" n'est pas dans la base de données, il y aura également un message d'erreur.

## Si je voulais prendre plus de temps
J'aurais :
- Ajouté une authentification via JWT pour que le champ "username" n'est plus à être remplis manuellement lors de la création des alertes. 
- Créée une interface 
- Ajouter des tests automatiques avec tox.ini

## Features en plus
J'ai choisis d'implémenter à la place du login, une création d'utilisateur directement via la requête avec POST.
Il suffit d'entrer un utilisateur comme ci-dessous :

    {
    "username" : "Marie1",
    "password" : "password1"
    }