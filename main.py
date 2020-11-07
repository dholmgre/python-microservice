from flask import Flask, render_template, make_response, jsonify, request

app = Flask(__name__)
PORT = 3200

INFO = {
    "languages": {
        "es": "Spanish",
        "us": "English US",
        "se": "Swedish"
    },
    "colors": {
        "r": "red",
        "g": "green",
        "b": "blue"
    },
    "clouds": {
        "IBM": "IBM CLOUD",
        "AWS": "AMAZON WEB SERVICES",
        "AZURE": "Microsoft AZURE"
    }
}

@app.route("/")
def home():
    return "<h1>this is home</h1>"

@app.route("/temp")
def yo():
    return render_template('index.html')

@app.route("/qstr")
def qs():
    if request.args:
        req = request.args
        res = {}
        for key, value in req.items():
            res[key] = value
        res = make_response(jsonify(res), 200)
        return res
    
    res =  make_response(jsonify({"error":"no arg in string"}), 404)
    return res


@app.route("/json")
def jsonInfo():
    res = make_response(jsonify(INFO), 200)
    return res

@app.route("/json/<collection>")
def get_collection(collection):
    if collection in INFO:
        collection = INFO[collection]
        if collection:
            return make_response(jsonify({"Collection":collection}), 200)
        return make_response(jsonify({"error":"Not found"}), 404)
    return make_response(jsonify({"error":"Not found"}), 404)


@app.route("/json/<collection>/<member>")
def get_member(collection, member):
    if collection in INFO:
        member = INFO[collection].get(member)
        if member:
            return make_response(jsonify({collection:member}), 200)
        return make_response(jsonify({"error":"Not found"}), 404)
    return make_response(jsonify({"error":"Not found"}), 404)


# POST METHOD
@app.route("/json/<collection>", methods=["POST"])
def add_cat(collection):
    req = request.get_json()
    if collection in INFO:
        res = make_response(jsonify({"error":"collection already exist"}), 400)
        return res
    
    INFO.update({collection: req})
    res = make_response(jsonify({"Success":"collection created"}), 200)
    return res


# PUT METHOD
@app.route("/json/<collection>/<member>", methods=["PUT"])
def updateJson(collection, member):
    req = request.get_json()
    if collection in INFO:
        print(req)
        INFO[collection][member] = req["new"]
        res = make_response(jsonify({"res":INFO[collection]}), 200)
        return res





if __name__ == "__main__":
    print("Server now running on port {}".format(PORT))
    app.run(host='localhost', port=PORT)
    