from flask import Flask
from flask_cors import CORS
from models import db

app = Flask(__name__)
CORS(app)  # To allow Cross-Origin requests from the frontend

# Database configuration (adjust as needed)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///exchange.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(app)

@app.route('/')
def home():
    return 'Crypto Exchange API is Running!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8002)
