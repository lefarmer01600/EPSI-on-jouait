## EPSI-on-jouait

Ce projet est une application web de quiz sur l'informatique et le marketing. Il est construit avec Flask, un framework web en Python, et utilise Tailwind CSS pour le style.

# Fonctionnement

L'application se compose de deux pages principales : une page d'accueil où l'utilisateur voit une question et peut choisir une réponse, et une page de réponse qui indique si la réponse de l'utilisateur était correcte ou non.

Les questions sont stockées dans un fichier JSON (questions_reponses.json). Chaque question a plusieurs options de réponse et une réponse correcte.

Lorsque l'utilisateur arrive sur la page d'accueil, une question est choisie au hasard parmi les catégories disponibles (Informatique_QCM, Marketing_QCM, Informatique_Vrai_Faux, Marketing_Vrai_Faux). La réponse correcte à cette question est stockée dans une variable globale.

Lorsque l'utilisateur soumet une réponse, la méthode submit est appelée. Cette méthode compare la réponse de l'utilisateur à la réponse correcte stockée précédemment. Si la réponse est correcte, l'utilisateur est redirigé vers la page de réponse avec un message indiquant que la réponse est correcte. Sinon, un message indiquant que la réponse est incorrecte est affiché.

# Installation

Pour installer et exécuter ce projet, vous devez avoir Python et Flask installés sur votre machine. Vous pouvez ensuite cloner ce dépôt et exécuter app.py pour démarrer l'application.

# Contribution

Les contributions à ce projet sont les bienvenues. Si vous souhaitez contribuer, veuillez créer une nouvelle branche, apporter vos modifications, puis soumettre une demande de merge.
