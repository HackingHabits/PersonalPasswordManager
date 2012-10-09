from config import MEDIA_FOLDER, TEMPLATE_FOLDER
from flask import Flask

app = Flask("PersonalPassword", template_folder=TEMPLATE_FOLDER, static_folder=MEDIA_FOLDER,static_path='/assets')
app.config.from_object('settings')

from google.appengine.ext import db
from google.appengine.api import users

from flask import redirect, url_for, request, render_template, abort, flash, get_flashed_messages

class SecretStore(db.Model):
    user = db.UserProperty(auto_current_user=True)
    website = db.StringProperty()
    password = db.StringProperty()
     
@app.route('/')
def index():
    user = users.get_current_user()
    passwds = SecretStore.all().filter('user =', user)
    return render_template('index.html', user=user, logout_url=users.create_logout_url("/"), passwds=passwds);

@app.route('/', methods=['POST'])
def passwd_post():
    website = request.form['website']
    password = request.form['password']
    if not website or not password:
        return redirect(url_for('index'))
    
    passwd = SecretStore(website = website, password=password)
    passwd.user = users.get_current_user()
    passwd.put()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def password_delete(id):
    passwd = SecretStore.get_by_id(id)
    if passwd and passwd.user == users.get_current_user():
        passwd.delete()
    else:
        abort(404)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
