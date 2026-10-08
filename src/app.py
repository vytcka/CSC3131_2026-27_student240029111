from flask import Flask
from extensions import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'

    db.init_app(app)
    from db_mitigation.book import Book

    with app.app_context():
        db.create_all()

    return app

    app = create_app()

    if __name__ == '__main__':
        app.run(debug=True)