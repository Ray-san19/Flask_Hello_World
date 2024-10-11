from flask import Flask
from flask import render_template
from flask import json
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/')
def hello_world():
    return "<h2>Bonjour à tout le monde !</h2><p>Pour accéder à vos exerices cliquez <a href='./exercices/'>Ici</a></p>"

@app.route('/exercices/')
def exercices():
    return render_template('exercices.html')

@app.route("/contact/")
def MaPremiereAPI():
    return render_template("contact.html")

@app.route('/somme/<int:valeur1>/<int:valeur2>')
def somme(valeur1, valeur2):
    resultat = valeur1 + valeur2
    return f"<h2>La somme de {valeur1} et {valeur2} est : {resultat}</h2>"


@app.route('/impairpair/<int:resultat>') 
def impairpair(resultat):
  if resultat % 2 == 0:
    return "Le résultat est pair"
  else :
    return "Le résultat est impair"

@app.route('/somme_global/<path:valeurs>')
def somme_global(valeurs):
  lst = valeurs.split('/')
  somme = int(lst[0])
  for i in range (len(lst)-1):
    somme += int(lst[i+1])
  return "La somme des éléments est:" + str(somme)

@app.route('/max/<path:valeurs>')
def max_value(valeurs):
    valeurs_list = list(map(int, valeurs.split('/')))
    valeur_max = valeurs_list[0]
    
    for valeur in valeurs_list:
        if valeur > valeur_max:
            valeur_max = valeur
    return f"<h2>La valeur la plus importante parmi {valeurs_list} est : {valeur_max}</h2>"
                                                                                                              
if __name__ == "__main__":
  app.run(debug=True)
