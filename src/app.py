from flask import Flask
from extensions import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'

    db.init_app(app)
    from db_mitigation.book import Book

    with app.app_context():
        db.create_all()

    collection = [
        new Book(title="Leadership's greatest virtue", author="Leonardo Hamato", review="Phanomenal book, no doubt about it!", rating=5),
        new Book(title="Science of materialising your ideas", author="Donatello Hamato", review="The idea is great, but the execution could be better.", rating=3),
        new Book(title="Art of muscle building", author="Raphael Hamato", review="unexpected views provided, very interesting!", rating=4),
        new Book(title="Once upon a time", author="Michelangelo Hamato", review="Nothing new views were provided, but phanomenal way of presenting them.", rating=2),
    ]
    for i in collection:
        db.session.add(i)
    db.session.commit()
    return app

    app = create_app()

    if __name__ == '__main__':
        app.run(debug=True)