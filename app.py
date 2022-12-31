
import gspread
from flask import Flask , render_template , request , redirect , url_for

gc = gspread.service_account(filename='simple-flask-portfolio.json')
sh = gc.open('simple-flask-portfolio')

shProfile = sh.get_worksheet(0)
shContact = sh.get_worksheet(1)

app = Flask(__name__)

@app.route('/' )
def home():


    profile = {
        'about': shProfile.acell('B1').value,
        'experience': shProfile.acell('B2').value,
        'interests': shProfile.acell('B3').value,
        'education': shProfile.acell('B4').value,
    }

    return render_template('index.html' , profile=profile)

@app.route('/contact', methods=['POST','GET']  )
def contact():

    if request.method == 'POST':
        shContact.append_row([ request.form['name'], request.form['email'], request.form['message']])

        return redirect(url_for('home'))

    return render_template('contact.html' )
