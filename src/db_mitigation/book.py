from flask_migrate import Migrate
from flask_wtf import FlaskForm

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    review = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def validate_review(self):
        if len(self.review) < 10:
            raise ValueError("Review must be at least 10 characters long.")
        if len(self.review) > 1000:
            raise ValueError("Review must not exceed 1000 characters.")

    def validate_rating(self):
        if self.rating < 1 or self.rating > 5:
            raise ValueError("Rating must be between 1 and 5.")

    def __repr__(self):
        return f'<Book {self.title} by {self.author}>'
    def __str__(self):
        return f'Book(title={self.title}, author={self.author}, review={self.review})'

