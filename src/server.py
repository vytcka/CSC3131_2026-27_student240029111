from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post_bookReview', methods=['POST'])
def post_bookReview():
    # Handle the POST request for submitting a book review
    pass

@app.route('/get_bookReviews', methods=['GET'])
def get_bookReviews():
    # Handle the GET request for retrieving book reviews
    pass

if __name__ == '__main__':
    app.run(debug=True)