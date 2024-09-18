from flask import Flask, render_template, request 
import json
import random

app = Flask(__name__)

cat = ['Informatique_QCM', 'Marketing_QCM', 'Informatique_Vrai_Faux', 'Marketing_Vrai_Faux']

data = {}

answer = ""

with open('src/questions_reponses.json', 'r') as file:
    data = json.load(file)

@app.route('/')
def home():
    global data, answer 
    question = data[random.choice(cat)][random.randint(0, len(data[random.choice(cat)])-1)]
    answer = question['correct_answer']
    return render_template('home.html', question=question)

@app.route('/submit', methods = ['POST'])
def submit():
    global answer
    if request.method == 'POST':
        user_answer = request.form.getlist('question')[0]
        print(user_answer)
        if user_answer == answer:
            return render_template('answer.html', reponse="Bonne réponse")
        return render_template('answer.html',reponse="Mauvaise réponse")
    return render_template('answer.html')
if __name__ == '__main__':
    app.run(debug=True)