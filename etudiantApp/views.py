from flask import Flask, render_template, request, jsonify, json, redirect
from flask_mongoengine import MongoEngine

from werkzeug.utils import secure_filename
import os

#  chemin absolu du projet
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
img_dir = os.path.join(APP_ROOT, 'static/img/')

#  Declaration de l'application et connection a la base
app = Flask(__name__) # name = etudiantApp.views
app.config['MONGODB_SETTINGS'] = {
    'db': 'db',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine()
db.init_app(app)


# SUPPRESSION PHOTO
def delete_photo(photo_name):
    place_file = "/".join([img_dir, photo_name])
    if os.path.exists(place_file):
        os.remove(place_file)
    else:
        pass

# declaration de la collection Etudiant_collection
class Etudiant_collection(db.Document):
    photo = db.StringField()
    nom = db.StringField()
    prenom = db.StringField()
    cycle = db.StringField()
    mention = db.StringField()
    username = db.StringField()

#  declaration de la collection Autentification
class Autentification(db.Document):
    username = db.StringField()
    pswd = db.StringField()

# page login de l'application
@app.route('/')
def index():
    return render_template('index.html')

#  verification de l'Autentification
@app.route('/login', methods=['GET', 'POST'])
def auth():
    username = request.form['username']
    pswdm = request.form['pswd']

    if Autentification.objects(username=username).first():
        return redirect('/home')
    else:
        return redirect('/')


# page centrale de l'application
@app.route('/home')
def home():
    etudiant = Etudiant_collection.objects.all()
    total = Etudiant_collection.objects.count()
    return render_template('home.html', etudiant=etudiant, total=total)

#  (create) collection Etudiant_collection
@app.route('/add', methods=['GET', 'POST'])
def add_etudiant():
    nom = request.form['nom']
    prenom = request.form['prenom']
    cycle = request.form['cycle']
    mention = request.form['mention']

    if request.files['photo']:
        photo_file = request.files['photo']
        # photo_file_name = secure_filename(photo_file.filename)
        photo_file_name = photo_file.filename
        destination = "/".join([img_dir, photo_file_name])
        photo_file.save(destination)

        Etudiant_collectionSave = Etudiant_collection(photo=photo_file_name,nom=nom, prenom=prenom, cycle=cycle, mention=mention)
        Etudiant_collectionSave.save()
    else:
        Etudiant_collectionSave = Etudiant_collection(photo=" Aucun ",nom=nom, prenom=prenom, cycle=cycle, mention=mention)
        Etudiant_collectionSave.save()
    return redirect('/home')

# (delete) de la collection Etudiant_collection
@app.route('/delete/<string:getid>', methods = ['POST','GET'])
def delete_etudiant(getid):
    # print(getid)
    etudiants = Etudiant_collection.objects(id=getid).first()
    if not etudiants:
        return jsonify({'error': ' Etudiant introuvable'})
    else:
        delete_photo(etudiants.photo)
        etudiants.delete()
    return redirect('/home')


#  recuperation des donnees a modifier
@app.route('/getOne', methods=['POST'])
def getOne_etudiant():
    pk = request.form['id']
    etudiant_rs = Etudiant_collection.objects(id=pk).first()
    return json.dumps(etudiant_rs)


#  (Update) MIse a jour de la collection Etudiant_collection
@app.route('/updateEtudiant', methods=['GET', 'POST'])
def updateemployee():
    pk = request.form['id']
    nom = request.form['nom']
    prenom = request.form['prenom']
    cycle = request.form['cycle']
    mention = request.form['mention']

    if request.files['photo']:
        photo_file = request.files['photo']
        # photo_file_name = secure_filename(photo_file.filename)
        photo_file_name = photo_file.filename
        destination = "/".join([img_dir, photo_file_name])
        photo_file.save(destination)

        etudiant_rs = Etudiant_collection.objects(id=pk).first()
        delete_photo(etudiant_rs.photo)
        etudiant_rs.update(photo=photo_file_name,nom=nom, prenom=prenom, cycle=cycle, mention=mention)
    else:
        etudiant_rs = Etudiant_collection.objects(id=pk).first()
        etudiant_rs.update(nom=nom, prenom=prenom, cycle=cycle, mention=mention)

    return redirect('/home')


if __name__ == "__main__":
    app.run(debug=True)
