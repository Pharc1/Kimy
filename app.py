from flask import Flask
from views import views
import os

app = Flask(__name__, static_folder='static')
app.register_blueprint(views)
app.secret_key = "secretsdqgd23425"

if __name__ == '__main__':
    app.run(debug=True, port=8000)