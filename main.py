from flask import Flask,jsonify
import csv

all_movies = []

with open('movies.csv',encoding = 'utf-8') as f:
    r = csv.reader(f)
    data = list(r)
    all_movies = data[1:]

liked_movies  = []
not_liked_movies = []
didnotwatch_movies = []

app = Flask(__name__)

@app.route("/")

def index():
    return "Welcome to movies homepage"

@app.route("/get_movies")
def get_movies():
    return jsonify({
        "data" : all_movies[0],
        "status" : "success"
    })

@app.route("/liked_movies",methods = ["POST"])
def likedMovies():
    global all_movies
    movie = all_movies[0]
    all_movies = all_movies[1:]
    liked_movies.append(movie)
    return jsonify({
        "status" : "success"
    }),200

@app.route("/not_liked_movies",methods = ["POST"])
def unliked_movies():
    global all_movies
    movie = all_movies[0]
    all_movies = all_movies[1:]
    not_liked_movies.append(movie)
    return jsonify({
        "status" : "success"
    }),200

@app.route("/didnotwatch_movies",methods = ["POST"])
def didnotWatch_movie():
    global all_movies
    movie = all_movies[0]
    all_movies = all_movies[1:]
    didnotwatch_movies.append(movie)
    return jsonify({
        "status": " success"
    }),200

if __name__ == "__main__" :
    app.run(debug = True)


