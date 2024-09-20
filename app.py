from flask import Flask, render_template, request 
import json
import random

# Création d'un serveur web Flask à partir du module flask
app = Flask(__name__)

# Catégories de questions
cat = ['Informatique_QCM', 'Marketing_QCM', 'Informatique_Vrai_Faux', 'Marketing_Vrai_Faux']

# Dictionnaire pour stocker les données des questions et réponses
data = {}

# Variable pour stocker la bonne réponse
answer = ""

# Ouvrir et lire le fichier JSON dans le dictionnaire data
with open('src/questions_reponses.json', 'r', encoding='utf8') as file:
    data = json.load(file)

# Définir la route de la page d'accueil
@app.route('/')
def home():
    global data, answer 
    # Sélectionner une question aléatoire dans les données
    question = data[random.choice(cat)][random.randint(0, len(data[random.choice(cat)])-1)]
    # Stocker la bonne réponse
    answer = question['correct_answer']
    # Rendre la page d'accueil avec la question sélectionnée
    return render_template('home.html', question=question)

# Définir la route pour soumettre les réponses
@app.route('/submit', methods = ['POST'])
def submit():
    global answer
    # Vérifier si la méthode est POST
    if request.method == 'POST':
        # Obtenir la réponse de l'utilisateur à partir du formulaire
        user_answer = request.form.getlist('question')[0]
        # Vérifier si la réponse de l'utilisateur est correcte
        if user_answer == answer:
            # Si c'est correct, rendre la page de réponse avec un message de succès
            return render_template('answer.html', reponse="Bonne réponse")
        # Si c'est incorrect, rendre la page de réponse avec un message d'échec
        return render_template('answer.html',reponse="Mauvaise réponse")
    # Si la méthode n'est pas POST, rendre simplement la page de réponse
    return render_template('answer.html')

# Exécuter l'application
if __name__ == '__main__':
    from waitress import serve
    # Servir l'application sur 0.0.0.0:8080
    serve(app, host="0.0.0.0", port=8080)
    # app.run(debug=True)
    # app.static_folder = 'static'