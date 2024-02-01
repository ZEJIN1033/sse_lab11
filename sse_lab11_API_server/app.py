from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

books = [
    {
        'id': 1,
        'title': 'To Kill a Mockingbird',
        'author': 'Harper Lee',
        'publication_year': 1960,
        'genre': 'Southern Gothic'
    },
    {
        'id': 2,
        'title': '1984',
        'author': 'George Orwell',
        'publication_year': 1949,
        'genre': 'Dystopian Fiction'
    },
    {
        'id': 3,
        'title': 'Pride and Prejudice',
        'author': 'Jane Austen',
        'publication_year': 1813,
        'genre': 'Romantic Novel'
    },
    {
        'id': 4,
        'title': 'The Great Gatsby',
        'author': 'F. Scott Fitzgerald',
        'publication_year': 1925,
        'genre': 'American Literature'
    },
    {
        'id': 5,
        'title': 'The Hunger Games',
        'author': 'Suzanne Collins',
        'publication_year': 2008,
        'genre': 'Young Adult Dystopian'
    }
]

@app.route('/', methods=['GET'])
def main():
    return render_template("index.html")

@app.route('/book', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/searchBook', methods=['GET'])
def search_book():
    title_query = request.args.get('title')
    author_query = request.args.get('author')
    publication_year_query = request.args.get('publication_year')
    genre_query = request.args.get('genre')
    filtered_books = []
    if title_query:
        filtered_books = [book for book in books if title_query.lower() in book['title'].lower()]
    elif author_query:
        filtered_books = [book for book in books if author_query.lower() in book['author'].lower()]
    elif publication_year_query:
        filtered_books = [book for book in books if publication_year_query.lower() in str(book['publication_year'])]
    elif genre_query:
        filtered_books = [book for book in books if genre_query.lower() in book['genre'].lower()]
    
    if filtered_books:
        return jsonify(filtered_books)
    else:
        return "Book not fund", 404


if __name__ == '__main__':
    app.run(debug=True)