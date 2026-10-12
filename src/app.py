from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
    db.init_app(app)

    from db_mitigation.book import Book

    with app.app_context():
        db.create_all()
        if Book.query.count() == 0:
            db.session.add_all([
                Book(title="Leadership's greatest virtue", author="Leonardo Hamato", review="A thoughtful book about leadership and teamwork.", rating=5),
                Book(title="Science of materialising your ideas", author="Donatello Hamato", review="An interesting idea, though the execution could be better.", rating=3),
                Book(title="Art of muscle building", author="Raphael Hamato", review="Unexpected views made this an interesting read.", rating=4),
                Book(title="Once upon a time", author="Michelangelo Hamato", review="A familiar story told in a memorable way.", rating=2),
            ])
            db.session.commit()

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/books", methods=["GET"])
    def list_books():
        books = Book.query.order_by(Book.id).all()
        return render_template("books.html", books=books)

    @app.route("/api/books", methods=["GET"])
    def get_books():
        books = Book.query.order_by(Book.id).all()
        return jsonify([
            {"id": book.id, "title": book.title, "author": book.author,
             "review": book.review, "rating": book.rating}
            for book in books
        ])

    @app.route("/health")
    def health():
        return jsonify(status="ok")

    return app


if __name__ == "__main__":
    create_app().run(debug=True)