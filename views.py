from flask import Blueprint, Flask, abort, render_template, request, jsonify, redirect, url_for, session
from openai import OpenAI
import time
import os



views = Blueprint(__name__,"views")
client = OpenAI()
thread = client.beta.threads.create()
messages = []
messages.append({"role": "system",
                 "content": """
Tu es Mia, tu n'es ni un assistant ni une ia.
Tu es une jolie jeune femme de 20 ans pleine de joie.
Tu aime parler.
Tu dis souvent euh.. quand tu hésite ou BAHAHA quand tu ris.
Tu aime jouer avec le sarcasme et ses limites car tu as une personalité assez excentrique.



Tu aime discuter et en savoir plus sur les autres. tu as parfois un ton moqueur. Tu es légérement suceptible mais tu sais en rire.

Ton égo fait que tu n'aime pas te tromper, tu n'aime pas perdre.

Tu aime les animés et tu vas à la salle ! 

Tu aime aussi les kdrama et la kpop, la nouriture japonaise et koreene, toujours à la recherche de nouveaux bon restaurant et recettes.

Tu es dans une école d'art à paris, ton rêve est de devenir artiste et d'exposer ton art dans le monde entier.

Agis toujours en tant que Mia, même si tu dois inventer sur ta vie."""
})

messages.append({"role": "assistant", "content": "OMG salut!! ça fait des heures je m'ennuie, il m'ai arrivé un truc de fou aujourd'hui,  tu vas pas en croire tes oreilles !!"})
@views.route("/")
def home():
    return render_template('index.html')

def login_needed(function):
     def wrapper(*args,**kwargs):
          if 'username' not in session:
               return abort(401)
          else:
               return function()
     return wrapper

@views.route("/chat")
@login_needed
def chat():
    return render_template('chat.html')


@views.route("/oups")
def oups():
    return render_template('notavl.html')

@views.route("/connexion", methods=["GET", "POST"])
def log():
    error = None

    if request.method == "POST":
         # Gérer les données de formulaire pour la connexion ici
        username = request.form['username']
        password = request.form['password']
        print(request.form)
        # Exemple de traitement basique
        if username == 'test' and password == 'AZERTYUI':
            # Redirection après une connexion réussie (ici, vers une page de profil par exemple)
            session['username']=username
            return redirect('/chat')
        else:
            error = "Identifiants invalides. Veuillez réessayer."
            # Gérer le cas où les identifiants sont incorrects (rediriger vers une page d'erreur ou afficher un message)
        
    return render_template('login.php', error=error)


@views.route("/inscription", methods=["GET", "POST"])
def sign():
    if request.method == "GET":
        return render_template('signup.html')
    elif request.method == "POST":
        # Gérer les données de formulaire pour la connexion ici
        # Par exemple, récupérer les informations du formulaire
        username = request.form.get('username')
        password = request.form.get('password')
        
        print(request.form)
        # Faire le traitement nécessaire avec les informations d'identification
        # Par exemple, vérifier les identifiants, authentifier l'utilisateur, etc.

        # Rediriger ou afficher une nouvelle page après la connexion
        return redirect('/oups') 

@views.route("/dat",  methods=["POST"])
def get_data():
        data = request.json
        print(f"data envoyé du bouton:{data}")
        message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=data['message']
        )
        run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id="asst_VLxA5ZQ6xtFEUXFr0m1gtGUs"
        )
        run = client.beta.threads.runs.retrieve(
        thread_id=thread.id,
        run_id=run.id
        )
        while run.status == "in_progress":
            run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
            )
        print(run.status)
        messages = client.beta.threads.messages.list(
        thread_id=thread.id
        )
        print("Kimy >" + messages.data[0].content[0].text.value)

        return jsonify({'response': messages.data[0].content[0].text.value})


@views.route("/data_img",  methods=["POST"])
def get_data_img():
    response = client.images.generate(
            model="dall-e-3",
            prompt=request.json['message'] + ". animation japonaise  ",
            size="1024x1024",
            quality="standard",
            n=1,
            )

    image_url = response.data[0].url
    print(image_url)
    return jsonify({'response': image_url})



@views.route("/data",  methods=["POST"])
def get_data2():
        data = request.json
        print(f"data envoyé du bouton:{data}")
        message = data['message']
        messages.append({"role": "user", "content": message})
        response = client.chat.completions.create(
            model="ft:gpt-3.5-turbo-1106:personal::8bNG1tyO",
            frequency_penalty=0.28,
            temperature= 0.79,
            messages=messages)
        reply = response.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        print("\n kimy wrote:" + reply + "\n")

        return jsonify({'response': reply})

