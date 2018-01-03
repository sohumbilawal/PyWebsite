from flask import Flask, render_template

app = Flask(__name__)

#Homepage start
@app.route('/')

def home():
    return render_template("home.html")
#Homepage end
#About page start
@app.route('/about/')

def about():
    return render_template("about.html")
#About page end

if __name__ == "__main__":
    app.run(debug = True)
