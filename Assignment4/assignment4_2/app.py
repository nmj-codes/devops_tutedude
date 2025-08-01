from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messages

# MongoDB Atlas connection string
MONGO_URI = "mongodb+srv://nandakishoremj3:nandu123@tram.hdgzlza.mongodb.net/?retryWrites=true&w=majority&appName=tram"
client = MongoClient(MONGO_URI)
db = client['mydatabase']
collection = db['mycollection']

@app.route('/form', methods=['GET'])
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form['name']
        email = request.form['email']

        if not name or not email:
            flash("Both name and email are required.")
            return render_template('form.html')

        # Insert into MongoDB
        collection.insert_one({'name': name, 'email': email})
        return redirect(url_for('success'))

    except Exception as e:
        flash(f"Error occurred: {str(e)}")
        return render_template('form.html')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
