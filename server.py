from flask import Flask, render_template, request, make_response, jsonify

from database import Database

app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/example_server_url_route", methods=["POST"])
def get_data_from_client():
    x = request.get_json()
    print(x)

    return make_response({"message":f"you said {x}!"}, 200)

@app.route("/api/books")
def get_books():
    with Database() as db:
        book_query = "SELECT * FROM Books"
        all_books = db.executeWrapper(book_query)
        print(all_books)
        books = parse_into_json(all_books)
    return books


def parse_into_json(data):
    jsonDicts = []
    for row in data:
        elementDict = {}
        listOfElements = ["id", "isbn", "title", "author", "publisher", "publish year", "category", "total copies", "available copies"]
        for i in range(0, len(listOfElements)):
            elementDict.update({listOfElements[i]: row[i]})
        jsonDicts.append(elementDict)
        
    
    return jsonDicts


if __name__ == "__main__":
    app.run(debug=True)