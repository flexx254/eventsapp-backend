from flask import Flask, jsonify
from supabase import create_client, Client
import os

app = Flask(__name__)

# Get environment variables from Render
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(url, key)

@app.route("/")
def home():
    return jsonify({"message": "Flask + Supabase + Render running!"})

@app.route("/test-supabase")
def test_supabase():
    try:
        data = supabase.table("users").select("*").execute()
        return jsonify(data.data)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
