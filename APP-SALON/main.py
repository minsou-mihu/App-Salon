import json
import os

from flask import Flask, redirect, render_template, request, session, url_for


def charger_stock_loreal():
    if os.path.exists("stock_loreal.json"):
        with open("stock_loreal.json", "r") as f:
            return json.load(f)
    return []

def enregistrer_produit_loreal(produit):
    stock = charger_stock_loreal()
    stock.append(produit)
    with open("stock_loreal.json", "w") as f:
        json.dump(stock, f, indent=2)

def charger_stock_brunoflaujac():
    if os.path.exists("stock_brunoflaujac.json"):
        with open("stock_brunoflaujac.json", "r") as f:
            return json.load(f)
    return []

def enregistrer_produit_brunoflaujac(produit):
    stock = charger_stock_brunoflaujac()
    stock.append(produit)
    with open("stock_brunoflaujac.json", "w") as f:
        json.dump(stock, f, indent=2)

def charger_stock_subtil():
    if os.path.exists("stock_subtil.json"):
        with open("stock_subtil.json", "r") as f:
            return json.load(f)
    return []

def enregistrer_produit_subtil(produit):
    stock = charger_stock_subtil()
    stock.append(produit)
    with open("stock_subtil.json", "w") as f:
        json.dump(stock, f, indent=2)

def charger_stock_natureeva():
    if os.path.exists("stock_natureeva.json"):
        with open("stock_natureeva.json", "r") as f:
            return json.load(f)
    return []

def enregistrer_produit_natureeva(produit):
    stock = charger_stock_natureeva()
    stock.append(produit)
    with open("stock_natureeva.json", "w") as f:
        json.dump(stock, f, indent=2)

def charger_stock_kerastase():
    if os.path.exists("stock_kerastase.json"):
        with open("stock_kerastase.json", "r") as f:
            return json.load(f)
    return []

def enregistrer_produit_kerastase(produit):
    stock = charger_stock_kerastase()
    stock.append(produit)
    with open("stock_kerastase.json", "w") as f:
        json.dump(stock, f, indent=2)

def charger_stock_ottokeunis():
    if os.path.exists("stock_ottokeunis.json"):
        with open("stock_ottokeunis.json", "r") as f:
            return json.load(f)
    return []

def enregistrer_produit_ottokeunis(produit):
    stock = charger_stock_ottokeunis()
    stock.append(produit)
    with open("stock_ottokeunis.json", "w") as f:
        json.dump(stock, f, indent=2)

def charger_stock_menstories():
    if os.path.exists("stock_menstories.json"):
        with open("stock_menstories.json", "r") as f:
            return json.load(f)
    return []

def enregistrer_produit_menstories(produit):
    stock = charger_stock_menstories()
    stock.append(produit)
    with open("stock_menstories.json", "w") as f:
        json.dump(stock, f, indent=2)

def charger_stock_johnnyverax():
    if os.path.exists("stock_johnnyverax.json"):
        with open("stock_johnnyverax.json", "r") as f:
            return json.load(f)
    return []

def enregistrer_produit_johnnyverax(produit):
    stock = charger_stock_johnnyverax()
    stock.append(produit)
    with open("stock_johnnyverax.json", "w") as f:
        json.dump(stock, f, indent=2)

def charger_stock_reborn():
    if os.path.exists("stock_reborn.json"):
        with open("stock_reborn.json", "r") as f:
            return json.load(f)
    return []

def enregistrer_produit_reborn(produit):
    stock = charger_stock_reborn()
    stock.append(produit)
    with open("stock_reborn.json", "w") as f:
        json.dump(stock, f, indent=2)


app = Flask(__name__)
app.secret_key = 'supersecret'  # à changer pour quelque chose de plus sûr en prod

# Utilisateurs
users = {
    "melanie": {
        "name": "Mélanie",
        "password": "2709",
        "photo": "melanie.jpg",
        "role": "admin"
    },
    "julie": {
        "name": "Julie",
        "password": "1234",
        "photo": "julie.jpg",
        "role": "admin"
    },
    "isais": {
        "name": "Isais",
        "password": "1234",
        "photo": "isais.jpg",
        "role": "user"
    },
}

produits_loreal = [
    {'nom': 'Dia Light', 'quantite': 6},
    {'nom': 'Blond Studio', 'quantite': 2},
    {'nom': 'INOA', 'quantite': 1}
]

@app.route("/")
def login_page():
    return render_template("login.html", users=users)


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    if username in users and users[username]["password"] == password:
        session["user"] = username
        return redirect(url_for("home"))
    else:
        return "Mot de passe incorrect", 403


@app.route("/home")
def home():
    if "user" not in session:
        return redirect(url_for("login_page"))

    user = users[session["user"]]
    return render_template('home.html', user=user)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


@app.route("/entree")
def entree():
    return render_template("entree.html")


@app.route("/sortie")
def sortie():
    return render_template("sortie.html")


@app.route("/inventaire")
def inventaire():
    return render_template("inventaire.html")


@app.route("/ficheproduits")
def ficheproduits():
    return render_template("ficheproduits.html")


@app.route("/rapport")
def rapport():
    return render_template("rapport.html")


@app.route("/reglages")
def reglages():
    return render_template("reglages.html")


@app.route('/settings')
def settings():
    if 'user' not in session:
        return redirect(url_for('login_page'))
    return render_template('settings.html')


@app.route('/update_password', methods=['POST'])
def update_password():
    username = session['user']
    old_password = request.form['old_password']
    new_password = request.form['new_password']

    if users[username]['password'] == old_password:
        users[username]['password'] = new_password
        return "Mot de passe mis à jour ! <a href='/settings'>Retour</a>"
    else:
        return "Mot de passe actuel incorrect. <a href='/settings'>Retour</a>"


@app.route('/update_photo', methods=['POST'])
def update_photo():
    username = session['user']
    photo = request.files['photo']
    if photo:
        filename = f"{username}.jpg"
        path = os.path.join('static/images', filename)
        photo.save(path)
        users[username]['photo'] = f"images/{filename}"
        return "Photo mise à jour ! <a href='/settings'>Retour</a>"
    else:
        return "Erreur lors de l'envoi du fichier."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

@app.route("/choix-fournisseur-entree")
def choix_fournisseur_entree():
    return render_template("choix_fournisseur_entree.html")
@app.route("/choix-fournisseur-inventaire")
def choix_fournisseur_inventaire():
    return render_template("choix_fournisseur_inventaire.html")

@app.route("/choix-fournisseur-fiche-produits")
def choix_fournisseur_fiches():
    return render_template("choix_fournisseur_fiches.html")

@app.route('/loreal', methods=['GET', 'POST'])
def page_loreal():
    if request.method == 'POST':
        produit = {
            'nom': request.form['nom'],
            'categorie': request.form['categorie'],
            'gamme': request.form['gamme'],
            'code_barres': request.form['code_barres'],
            'quantite': 0 # par défaut
        }
        enregistrer_produit_loreal(produit)

    stock = charger_stock_loreal()
    return render_template('fiche_fournisseur.html', fournisseur="L'Oréal", produits=stock)

@app.route('/brunoflaujac', methods=['GET', 'POST'])
def page_brunoflaujac():
    if request.method == 'POST':
        produit = {
            'nom': request.form['nom'],
            'categorie': request.form['categorie'],
            'gamme': request.form['gamme'],
            'code_barres': request.form['code_barres'],
            'quantite': 0 # par défaut
        }
        enregistrer_produit_brunoflaujac(produit)

    stock = charger_stock_brunoflaujac()
    return render_template('fiche_fournisseur.html', fournisseur="Bruno Flaujac", produits=stock)

@app.route('/subtil', methods=['GET', 'POST'])
def page_subtil():
    if request.method == 'POST':
        produit = {
            'nom': request.form['nom'],
            'categorie': request.form['categorie'],
            'gamme': request.form['gamme'],
            'code_barres': request.form['code_barres'],
            'quantite': 0 # par défaut
        }
        enregistrer_produit_subtil(produit)

    stock = charger_stock_subtil()
    return render_template('fiche_fournisseur.html', fournisseur="Subtil", produits=stock)

@app.route('/natureeva', methods=['GET', 'POST'])
def page_natureeva():
    if request.method == 'POST':
        produit = {
            'nom': request.form['nom'],
            'categorie': request.form['categorie'],
            'gamme': request.form['gamme'],
            'code_barres': request.form['code_barres'],
            'quantite': 0 # par défaut
        }
        enregistrer_produit_natureeva(produit)

    stock = charger_stock_natureeva()
    return render_template('fiche_fournisseur.html', fournisseur="Nature Eva", produits=stock)

@app.route('/kerastase', methods=['GET', 'POST'])
def page_kerastase():
    if request.method == 'POST':
        produit = {
            'nom': request.form['nom'],
            'categorie': request.form['categorie'],
            'gamme': request.form['gamme'],
            'code_barres': request.form['code_barres'],
            'quantite': 0 # par défaut
        }
        enregistrer_produit_kerastase(produit)

    stock = charger_stock_kerastase()
    return render_template('fiche_fournisseur.html', fournisseur="Kerastase", produits=stock)

@app.route('/ottokeunis', methods=['GET', 'POST'])
def page_ottokeunis():
    if request.method == 'POST':
        produit = {
            'nom': request.form['nom'],
            'categorie': request.form['categorie'],
            'gamme': request.form['gamme'],
            'code_barres': request.form['code_barres'],
            'quantite': 0 # par défaut
        }
        enregistrer_produit_ottokeunis(produit)

    stock = charger_stock_ottokeunis()
    return render_template('fiche_fournisseur.html', fournisseur="Otto Keunis", produits=stock)

@app.route('/menstories', methods=['GET', 'POST'])
def page_menstories():
    if request.method == 'POST':
        produit = {
            'nom': request.form['nom'],
            'categorie': request.form['categorie'],
            'gamme': request.form['gamme'],
            'code_barres': request.form['code_barres'],
            'quantite': 0 # par défaut
        }
        enregistrer_produit_menstories(produit)

    stock = charger_stock_menstories()
    return render_template('fiche_fournisseur.html', fournisseur="Men Stories", produits=stock)

@app.route('/johnnyverax', methods=['GET', 'POST'])
def page_johnnyverax():
    if request.method == 'POST':
        produit = {
            'nom': request.form['nom'],
            'categorie': request.form['categorie'],
            'gamme': request.form['gamme'],
            'code_barres': request.form['code_barres'],
            'quantite': 0 # par défaut
        }
        enregistrer_produit_johnnyverax(produit)

    stock = charger_stock_johnnyverax()
    return render_template('fiche_fournisseur.html', fournisseur="Johnny Verax", produits=stock)

@app.route('/reborn', methods=['GET', 'POST'])
def page_reborn():
    if request.method == 'POST':
        produit = {
            'nom': request.form['nom'],
            'categorie': request.form['categorie'],
            'gamme': request.form['gamme'],
            'code_barres': request.form['code_barres'],
            'quantite': 0 # par défaut
        }
        enregistrer_produit_reborn(produit)

    stock = charger_stock_reborn()
    return render_template('fiche_fournisseur.html', fournisseur="Re Born", produits=stock)