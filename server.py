import flask from Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return rendet_template('index.html')
