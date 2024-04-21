from flask import Flask, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/dbname'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(255), nullable=False)
    short_code = db.Column(db.String(10), unique=True, nullable=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form['url']
        short_code = generate_short_code()
        new_url = URL(original_url=original_url, short_code=short_code)
        db.session.add(new_url)
        db.session.commit()
        return redirect(url_for('redirect_to_original', short_code=short_code))
    return '''
        <form method="post">
            <input type="text" name="url" placeholder="Enter URL" required>
            <input type="submit" value="Shorten">
        </form>
    '''

def generate_short_code():
    short_code = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    if not URL.query.filter_by(short_code=short_code).first():
        return short_code
    else:
        return generate_short_code()

@app.route('/<short_code>')
def redirect_to_original(short_code):
    original_url = URL.query.filter_by(short_code=short_code).first().original_url
    return redirect(original_url)

if __name__ == '__main__':
    app.run(debug=True)