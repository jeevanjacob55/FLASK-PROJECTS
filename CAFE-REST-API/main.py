from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random
app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)
    
    #conver to dict
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "location": self.location,
            "seats": self.seats,
            "has_wifi": self.has_wifi,
            "has_toilets":self.has_sockets,
            "has_toilet": self.has_toilet,
            "has_sockets":self.has_sockets,
            "can_take_calls":self.can_take_calls,
            "map_url":self.map_url,
            "img_url":self.img_url
        }
    

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

#get a random cafe data
@app.route("/random", methods=["GET"])
def get_random_cafe():
    cafes = Cafe.query.all()
    if cafes:
        random_cafe = random.choice(cafes)
        return jsonify(random_cafe.to_dict())
    else:
        return jsonify({"error": "No cafes found"}), 404
      # Custom structured response -Use when you need to create a custom response
        # response = {
        #     "name": cafe.name,
        #     "location": cafe.location,
        #     "amenities": {
        #         "wifi": cafe.has_wifi,
        #         "sockets": cafe.has_sockets,
        #         "toilet": cafe.has_toilet,
        #         "can_take_calls": cafe.can_take_calls
        #     },
        # }

#get the list of all cafes
@app.route("/all", methods=["GET"])
def get_all_cafes():
    cafes = Cafe.query.all()
    result = [cafe.to_dict() for cafe in cafes]
    return jsonify(result)

#get request which passes the location of the cafe as an argument
@app.route("/search", methods=["GET"])
def search_cafes():
    location_query = request.args.get("loc")  # ?loc=Chelakkara

    if not location_query:
        return jsonify({"error": "Please provide a 'loc' query parameter."}), 400

    cafes = Cafe.query.filter(Cafe.location.ilike(f"%{location_query}%")).all()

    if cafes:
        result = [cafe.to_dict() for cafe in cafes]
        return jsonify(result)
    else:
        return jsonify({"error": f"No cafes found at location: {location_query}"}), 404

# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_cafe():
    try:
        new_cafe = Cafe(
            name=request.form.get("name"),
            map_url=request.form.get("map_url"),
            location=request.form.get("location"),
            has_wifi=bool(int(request.form.get("has_wifi"))),
            has_sockets=bool(int(request.form.get("has_sockets"))),
            has_toilet=bool(int(request.form.get("has_toilet"))),
            can_take_calls=bool(int(request.form.get("can_take_calls"))),
            img_url =request.form.get("img_url")
        )

        db.session.add(new_cafe) #add cafe to the table
        db.session.commit()
        return jsonify({"success": "New cafe added!"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 400


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    new_price = request.form.get("new_price")

    if not new_price:
        return jsonify({"error": "Missing 'new_price' in request"}), 400

    try:
        cafe = Cafe.query.get(cafe_id)
        if cafe:
            cafe.coffee_price = new_price
            db.session.commit()
            return jsonify({"success": f"Updated coffee price to {new_price} for cafe ID {cafe_id}"}), 200
        else:
            return jsonify({"error": f"Cafe with ID {cafe_id} not found."}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api_key") #get the argument passed after ?
    
    # api verification
    if api_key != "TopSecretAPIKey":
        return jsonify({"error": "You are not authorized to perform this action."}), 403

    # Try to find the cafe
    cafe = Cafe.query.get(cafe_id) #get cafe by cafe_id
    if cafe:
        db.session.delete(cafe)
        db.session.commit()
        return jsonify({"success": f"Cafe with ID {cafe_id} has been deleted."}), 200
    else:
        return jsonify({"error": f"No cafe found with ID {cafe_id}."}), 404


if __name__ == '__main__':
    app.run(debug=True)
