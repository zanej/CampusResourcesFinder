from flask import Flask, render_template, jsonify, request
import sqlite3
import json
import os

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('resources.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/resources')
def get_resources():
    category = request.args.get('category')
    lang = request.args.get('lang', 'en')  # Default to English
    conn = get_db_connection()

    query = 'SELECT * FROM resources WHERE language = ?'
    params = [lang]

    if category:
        query += ' AND category = ?'
        params.append(category)

    resources = conn.execute(query, params).fetchall()
    conn.close()
    return jsonify([dict(row) for row in resources])

@app.route('/api/buses')
def get_bus_data():
    try:
        with open('static/bus_data.json', 'r') as f:
            return jsonify(json.load(f))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
