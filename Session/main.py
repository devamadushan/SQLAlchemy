from flask import Flask, request, redirect, url_for, render_template
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table, text
from conn import ENGINE, cursor

app = Flask(__name__)

# Définition de la table "utilisateurs"
metadata = MetaData()
utilisateur_table = Table(
    'utilisateurs', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('utilisateur', String(255), nullable=False),
    Column('mot_de_passe', String(255), nullable=False)
)
# Création de la table dans la base de données
metadata.create_all(ENGINE)

query = text("select * from utilisateurs;")
lesUtilisateurs = cursor.execute(query)


@app.route('/inscription')
def inscript():
    return render_template('form.html')


@app.route('/hello')
def index():
    return render_template('index.html')


@app.route('/utilisateurs')
def listeUtilisateurs():
    return render_template('listUtilisateurs.html', utilisateur=lesUtilisateurs)


@app.route('/submit', methods=['POST'])
def submit():
    nom_utilisateur = request.form['nom_utilisateur']
    mot_de_passe = request.form['mot_de_passe']

    # Insertion des données dans la base de données
    utilisateur = utilisateur_table.insert().values(utilisateur=nom_utilisateur, mot_de_passe=mot_de_passe)
    cursor.execute(utilisateur)
    cursor.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
