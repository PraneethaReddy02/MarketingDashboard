# Import necessary modules from Flask and Python standard libraries
from flask import Flask, render_template, jsonify
import os
import json

# Initialize the Flask application
app = Flask(__name__)

# Route for the main dashboard page.
# This route renders the index.html file located in the /templates folder.
@app.route('/')
def index():
    return render_template("index.html")

# API endpoint to serve market share data.
# Reads data from /data/marketshare.json and returns it as JSON.
@app.route('/api/marketshare')
def api_marketshare():
    # Construct the path to the marketshare.json file
    filepath = os.path.join(app.root_path, "data", "marketshare.json")
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
    except Exception as e:
        return jsonify({"error": "Failed to load market share data", "details": str(e)}), 500
    return jsonify(data)

# API endpoint to serve revenue trends data.
# Reads data from /data/revenuetrends.json and returns it as JSON.
@app.route('/api/revenuetrends')
def api_revenuetrends():
    # Construct the path to the revenuetrends.json file
    filepath = os.path.join(app.root_path, "data", "revenuetrends.json")
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
    except Exception as e:
        return jsonify({"error": "Failed to load revenue trends data", "details": str(e)}), 500
    return jsonify(data)

# API endpoint to serve market segmentation data.
# Reads data from /data/marketsegment.json and returns it as JSON.
@app.route('/api/marketsegment')
def api_marketsegment():
    # Construct the path to the marketsegment.json file
    filepath = os.path.join(app.root_path, "data", "marketsegment.json")
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
    except Exception as e:
        return jsonify({"error": "Failed to load market segmentation data", "details": str(e)}), 500
    return jsonify(data)

# If this script is run directly, start the Flask development server.
if __name__ == '__main__':
    # Enable debug mode for development; set to False in production.
    app.run(debug=True)
