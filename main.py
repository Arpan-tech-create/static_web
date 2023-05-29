from flask import Flask,render_template

app = Flask(__name__,template_folder='templates')

@app.route('/')
def main():

    return render_template('index.html')

@app.route('/con')
def main1():

    return render_template('contact.html')

@app.route('/abt')
def about():

    return render_template('about.html')


app.run(debug=True)