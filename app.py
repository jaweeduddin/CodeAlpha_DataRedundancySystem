from flask import Flask, request, render_template, redirect
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Atlas Connection
client = MongoClient("mongodb+srv://abrarruddin1234_db_user:syram8B1aRVbh7aS@codealphacluster.cmnvxfv.mongodb.net/?appName=CodeAlphaCluster")

# Database
db = client["CodeAlphaDB"]

# Collection
collection = db["users"]

@app.route('/')
def home():

    users = collection.find()

    return render_template(
        "index.html",
        users=users
    )

@app.route('/add', methods=['POST'])
def add_data():

    name = request.form['name']
    email = request.form['email']

    existing_user = collection.find_one({"email": email})

    if existing_user:
        users = collection.find()

        return render_template(
            "index.html",
            message="Duplicate Data Found! Email already exists.",
            color="red",
            users=users
        )

    collection.insert_one({
        "name": name,
        "email": email
    })

    return redirect('/')

@app.route('/delete/<email>')
def delete_user(email):

    collection.delete_one({"email": email})

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)