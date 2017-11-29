from Flask, import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    template = jinja_env.get_template('account.html')
    return render_template('account.html')

