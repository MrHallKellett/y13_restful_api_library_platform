from flask import Flask, render_template, request, make_response


app = Flask(__name__)



@app.route("/")
def index():
    return render_template("example_index.html")

@app.route("/example_server_url_route", methods=["POST"])
def get_data_from_client():
    x = request.get_json()
    print(x)

    return make_response({"message":f"you said {x}!"}, 200)


if __name__ == "__main__":
    app.run(debug=True)