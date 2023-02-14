#Esercizio:
#realizzare un server web con flask che offra le seguenti funzionalità.
#1. homepage deve fornire una breve descrizione delle caratteristiche della città di milano
#2. al link <nome sito>/immagini deve essere visualizzate le immagini di 4 monumenti di milano (controllare sul sito del prof come si fa a mettere le immagini)
#3. fare in modo che cliccando sull'immagine si venga mandati ad un brevo testo descrittivo del monumento (sito prof)


from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def milano():
    return render_template('milano.html')

@app.route("/immagini")
def monumenti():
    return render_template("immagini.html")

@app.route("/duomo")
def duomo():
    return render_template("duomo.html")

@app.route("/castello")
def castello():
    return render_template("castello.html")

@app.route("/cenacolo")
def cenacolo():
    return render_template("cenacolo.html")

@app.route("/sansiro")
def sansiro():
    return render_template("san_siro.html")


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)