# 🏊 Cafe-Data

This project is a Flask-based web application that showcases advanced **WTForms** features, including emoji-powered dropdowns, safe form handling, and CSV file writing. It's styled with **Bootstrap-Flask** to ensure clean UI integration.

---

## 🚀 Features Implemented

### 📋 Form Fields with Emoji SelectFields

This app includes user-friendly form fields powered by emoji ratings:

* **Coffee Rating**: `☕` to `☕☕☕☕☕`
* **Wi-Fi Rating**: `✘` to `💪💪💪💪💪`
* **Power Rating**: `✘` to `🔌🔌🔌🔌🔌`

Each dropdown uses the `SelectField` with a tuple structure like:

```python
('💪💪', '💪💪')
```

This stores the first value and displays the second.

---

### 📨 Form Handling and Submission

* Data is retrieved using `request.form.get('field_name')` for safety.
* Avoided using dot notation (e.g., `form.name.data`) to prevent common pitfalls.
* Renamed reserved keywords like `open` to `opening_time`.

---

### 📅 CSV Writing

On successful form submission, cafe details are written to `cafe-data.csv`:

```python
with open('cafe-data.csv', mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow([name, location, opening_time, close, coffee, wifi, power])
```

Tips:

* `newline=''` avoids blank lines on Windows.
* Ensure the existing CSV ends with a newline to prevent misaligned rows.

---

### 🌟 Bootstrap-Enhanced UI

Used `render_form(form)` from Bootstrap-Flask for clean rendering:

```jinja
{% from 'bootstrap5/form.html' import render_form %}
{{ render_form(form) }}
```

Potential enhancements:

* Add success flash messages
* Redirect to cafe list or home page
* Display submitted data in real-time

---

## 📚 Tech Stack

* Python 3.10+
* Flask
* Flask-WTF
* Bootstrap-Flask
* WTForms
* CSV module

---

## 🚩 How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/flask-cafe-form
cd flask-cafe-form
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the Flask app:

```bash
flask run
```

---

## 🧱 Author

**Jeevan Jacob** | **100 days of code**
B.Tech CSE | Python Enthusiast

---

> If you liked this project, give it a star ⭐ and explore more Flask apps in my [Flask Project Repo](https://github.com/jeevanjacob55/FLASK-PROJECTS)!
