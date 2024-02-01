from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

# Set as the environment variable in azure, if not works from github, use the 
# commented api_url
api_url = os.environ.get("API_URL")
# api_url = "http://querybooks.cvgwf7egf2gudwg5.uksouth.azurecontainer.io:5000/book"

@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/allbooks', methods=['GET'])
def books():
    url = api_url
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
    return render_template('books.html', data = data)

@app.route('/querytitle', methods=['GET'])
def querytitle():
    if request.method == 'GET':
        query = request.args.get('title')

        if query:
            url = api_url
            response = requests.get(url)
            if response.status_code == 200:
                data_get = response.json()
                data = []
                for book in data_get:
                    if book['title'].lower() == query.lower():
                        data.append(book)                
                if data != []:
                    return render_template('books.html', data = data)
                else:
                    return "Book Not found", 404
        else:
            return "No title provided", 404


@app.route('/queryid', methods=['GET'])
def queryid():
    if request.method == 'GET':
        query = request.args.get('id')

        if query:
            url = api_url
            response = requests.get(url)
            if response.status_code == 200:
                data_get = response.json()
                data = []
                for book in data_get:
                    if str(book['id']) == str(query):
                        data.append(book)                
                if data != []:
                    return render_template('books.html', data = data)
                else:
                    return "Book Not found", 404
        else:
            return "No id provided", 404


@app.route('/searchbook', methods=['GET', 'POST'])
def searchBook():
    if request.method == 'GET':
        search_type = request.args.get('searchType')
        query_value = request.args.get('query')
        url = f"http://querybooks.cvgwf7egf2gudwg5.uksouth.azurecontainer.io:5000/searchBook?{search_type}={query_value}"
        response = requests.get(url)
        print(response.status_code)
        if response.status_code == 200:
            data = response.json()
            return render_template('books.html', data = data)
        else:
            return f"{response.status_code} {response.text}"
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)