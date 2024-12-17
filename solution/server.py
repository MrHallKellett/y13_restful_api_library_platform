from flask import Flask, render_template, request, make_response
from cats import process_cats

app = Flask(__name__)



@app.route("/")
def index():
    return render_template("example_index.html")


@app.route("/api/cats")
def get_cats():
    return make_response({"message":process_cats(), 200})

@app.route("/example_server_url_route", methods=["POST"])
def get_data_from_client():
    x = request.get_json()
    print(x)

    return make_response({"message":f"you said {x}!"}, 200)


if __name__ == "__main__":
    app.run(debug=True)