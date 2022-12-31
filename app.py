
import gspread
from flask import Flask , render_template , request

gc = gspread.service_account(filename='simple-flask-portfolio.json')
sh = gc.open('simple-flask-portfolio')

shProfile = sh.get_worksheet(0)
shContact = sh.get_worksheet(1)

# shEducation = sh.get_worksheet(2)
# shExperience = sh.get_worksheet(3)


app = Flask(__name__)

@app.route('/' , methods=['POST','GET']  )
def home():

    if request.method == 'POST':
        shContact.append_row([ request.form['name'], request.form['email'], request.form['message']])

    profile = {
        'about': shProfile.acell('B1').value,
        'experience': shProfile.acell('B2').value,
        'interests': shProfile.acell('B3').value,
        'education': shProfile.acell('B4').value,
    }
    return render_template('index.html' , profile=profile)

@app.route('/contact' )
def contact():
    # contact = {
    #     'name': shContact.acell('A1').value,
    #     'email': shContact.acell('B1').value,
    # }
    return render_template('contact.html' )
