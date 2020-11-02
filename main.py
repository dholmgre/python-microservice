from flask import Flask, render_template, make_response, jsonify, request

app = Flask(__name__)

PORT = 3200

@app.route("/")
def home():
    return "<h1>this is home</h1>"

@app.route("/temp")
def yo():
    return render_template('index.html')



if __name__ == "__main__":
    print("Server now running on port {}".format(PORT))
    app.run(host='localhost', port=PORT)
    