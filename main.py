from flask import Flask, render_template

app=Flask(__name__)#MODEL

@app.route("/")#CONTROLLER
def index():
    return render_template("index.html")#VIEW

@app.route("/about")#CONTROLLER
def about_me():
    return render_template("about.html")#VIEW

@app.route("/festivalplattform-subpage")#CONTROLLER
def cats():
    return render_template("festivalplattform-subpage.html")#VIEW

if __name__ == '__main__':
    app.run()

