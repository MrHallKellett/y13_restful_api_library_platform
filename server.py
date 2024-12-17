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
        all_books = db.execute_wrapper(book_query)
        print(all_books)
        books = parse_into_json(all_books)
    return books


def parse_into_json(data):
    all_books = []
    for row in data:
        book = {}
        fields = ["id", "isbn", "title", "author", "publisher", "publish year", "category", "total copies", "available copies"]
        for i in range(len(fields)):
            book.update({fields[i]: row[i]})
        all_books.append(book)
        
    
    return all_books


if __name__ == "__main__":
    app.run(debug=True)