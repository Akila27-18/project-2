from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/greet/<name>')
def greet(name):
    lang = request.args.get('lang', 'en')
    greetings = {
        'en': 'Hello',
        'fr': 'Bonjour',
        'es': 'Hola',
        'ta': 'வணக்கம்',
        'hi': 'नमस्ते'
    }
    greeting = greetings.get(lang, greetings['en'])
    return render_template('greet.html', name=name, greeting=greeting, lang=lang)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    lang = request.form['lang']
    return redirect(url_for('greet', name=name, lang=lang))

if __name__ == '__main__':
    app.run(debug=True)
