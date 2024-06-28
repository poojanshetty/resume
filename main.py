from flask import Flask, render_template


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SECRET_KEY'] = 'hard_to_guess_string'  # os.urandom(16).hex()


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)
