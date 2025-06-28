# 🍯 Cafe Explorer API

A Flask-based RESTful API for managing and retrieving cafe data, including amenities, location, and coffee prices. Built with SQLAlchemy, this project allows CRUD operations on a SQLite database of cafes.

---

## 📅 Features

* 🌉 View a random cafe
* 📂 Get all cafes
* 🔍 Search cafes by location
* ➕ Add new cafes via POST requests
* ✏️ Update coffee prices via PATCH
* ❌ Delete cafes with API key authentication

---

## 🚀 Tech Stack

* Python 3
* Flask
* SQLAlchemy ORM
* SQLite
* Jinja2 Templates (for homepage only)

---

## 🔧 Setup & Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/cafe-explorer-api.git
   cd cafe-explorer-api
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**

   ```bash
   flask run  # or python main.py
   ```

---

## 🌐 API Endpoints

### `/`

Homepage (simple HTML render)

### `/random`

**GET** a random cafe

### `/all`

**GET** all cafes as JSON

### `/search?loc=LocationName`

**GET** cafes matching location (case-insensitive)

### `/add`

**POST** a new cafe

**Form Data Required:**

* `name`, `map_url`, `location`, `img_url`
* `has_wifi`, `has_sockets`, `has_toilet`, `can_take_calls` (as 0 or 1)

### `/update-price/<int:cafe_id>`

**PATCH** a cafe's coffee price

**Form Data Required:**

* `new_price`

### `/report-closed/<int:cafe_id>?api_key=TopSecretAPIKey`

**DELETE** a cafe record (requires API key)

---


