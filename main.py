from flask import Flask, request, redirect, render_template
import jinja2
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

@app.route("/")
def index():
    template = jinja_env.get_template('account.html')
    return render_template('account.html')

@app.route("/account.html", methods=['POST'])
def greeting():
    first_name = request.form['first_name']
    
    return render_template('hello_greeting.html', name=first_name)





app.run()