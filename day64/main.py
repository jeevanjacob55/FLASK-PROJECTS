from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, SelectField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
Bootstrap5(app)
class Editform(FlaskForm):
    rating = FloatField("Your Rating (0-10)", validators=[DataRequired()])
    review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField("Update")

class Addform(Flaskform):
    title = SelectField("Name of the Movie",validators=[DataRequired()])

class Base(DeclarativeBase):
    pass
db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Movie(Base):
    __tablename__ = 'movies' 

    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    name:Mapped[str] = mapped_column(String(250),nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

with app.app_context():
    db.create_all()

def add_movies():
    new_movie = Movie(
    name="Phone Booth",
    year=2002,
    description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    rating=7.3,
    ranking=10,
    review="My favourite character was the caller.",
    img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg")

    second_movie = Movie(
    name="Avatar The Way of Water",
    year=2022,
    description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
    rating=7.3,
    ranking=9,
    review="I liked the water.",
    img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg")
    
    with app.app_context():
        db.session.add(new_movie)
        db.session.add(second_movie)
        db.session.commit()
    
# add_movies()
# CREATE TABLE
@app.route("/")
def home():
    result = db.session.execute(db.select(Movie))
    all_movies = result.scalars().all()
    return render_template("index.html", movies=all_movies)
@app.route('/edit/<int:id>',methods = ["GET","POST"])
def edit(id):
    movie = db.session.get(Movie, id)  # Retrieve movie by ID
    form = Editform() # Pre-fill form with existing data

    if form.validate_on_submit():
        movie.rating = form.rating.data  # Update rating
        movie.review = form.review.data  # Update review
        db.session.commit()  # Save changes to the database
        return redirect(url_for("home"))  # Redirect to home page

    return render_template("edit.html", form=form, movie=movie)
@app.route("/delete/<int:id>")
def delete(id):
    movie = db.session.get(Movie, id)  # Get movie by ID
    if movie:
        db.session.delete(movie)  # Delete movie from database
        db.session.commit()  # Commit changes
    return redirect(url_for("home"))    

@app.route('/add')
def add():
    return render_template('add.html')
if __name__ == '__main__':
    app.run(debug=True)
