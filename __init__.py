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


@app.route('/impairpair/<resultat') 
def impairpair(resultat):
  if resultat % 2 == 0:
    return "Le résultat est pair"
  else :
    return "Le résultat est impair"
                                                                                                              
if __name__ == "__main__":
  app.run(debug=True)
