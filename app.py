from flask import Flask, render_template, request, redirect, url_for, session, flash


app = Flask(__name__)


@app.route('/')
def index():
        return redirect(url_for('home'))

@app.route('/user')
def user():
        return redirect(url_for('user.html'))

@app.route('/main')
def main():
      return render_template('index.html')



@app.route('/home')
def home():
    return render_template('home.html')
 

@app.route('/about')
def about():
    return render_template('about.html')
 
@app.route('/contact')
def contact():
        return redirect(url_for('login'))









if __name__ == '__main__':
    app.run(debug=True)
