from flask import Flask, render_template
from python import familug
from jobs import jobs
from home import homepg


app = Flask(__name__)
app.register_blueprint(familug)
app.register_blueprint(jobs)
app.register_blueprint(homepg)


if __name__ == "__main__":
    app.run(debug= True)