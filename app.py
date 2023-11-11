from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from trade_analysis import trade_analysis

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy()
db.init_app(app)


# CREATE TABLE IN DB
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
 
 
with app.app_context():
    db.create_all()

@app.route('/xxxxx')
def home2():
    return render_template("welcome.html")


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['POST', "GET"])
def register():
    return render_template("register.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/secrets')
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
def logout():
    pass


@app.route('/download')
def download():
    return send_from_directory('static', path="files/cheat_sheet.pdf", as_attachment=True)

@app.route('/trading', methods=['POST', 'GET'])
def recommendations():
    if request.method == 'POST':
        ticker = request.form.get('ticker')
        analysis = trade_analysis(ticker)
        return render_template('recommendation.html', ticker=ticker, analysis=analysis)
    return render_template('recommendation.html')
 
        
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=9090)


