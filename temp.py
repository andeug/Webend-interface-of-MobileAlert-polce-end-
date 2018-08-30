
from flask import Flask, flash,  render_template, request, session

app = Flask(__name__,template_folder="crimealert_folder")
app.secret_key = "super secret key"





 
  
@app.route('/')
def intro():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return home()
 
@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'letmeinn' and request.form['username'] == 'andrew':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return intro()

@app.route('/home')
def home():
    return render_template('home.html')
    
@app.route('/witness')
def witness():
    return render_template('WitnessList.html')

@app.route('/suspect')
def suspect():
    return render_template('SuspectList.html')
    
@app.route('/weeklyreport')
def weeklyreport():
    return render_template('weeklyreport.html')

@app.route('/heatmap')
def heatmap():
    return render_template('hotspot.html')

@app.route('/genderanalysis')
def genderanalysis():
    return render_template('gender_prediction.html')
    
@app.route('/prediction')
def prediction():
    return render_template('crime_prediction.html')
    
@app.route('/about')
def about():
    return render_template('policestation.html')

@app.route('/downloads')
def downloads():
    return render_template('downloads.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')




@app.route("/logout")
def logout():
    session['logged_in'] = False
    return intro()


if __name__ == '__main__':
  
    
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True,host='0.0.0.0', port=5000)
    app.run(debug=True, use_reloader=True)