from flask import Flask, jsonify
from supabase import create_client, Client
import os
from flask import request

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





@app.route("/signup", methods=["POST"])
def signup():
    try:
        data = request.json
        fullname = data.get("fullname")
        email = data.get("email")
        password = data.get("password")

        # ✅ Basic validation
        if not fullname or not email or not password:
            return jsonify({"error": "All fields are required"}), 400

        # ✅ Check if email already exists
        existing = supabase.table("users").select("*").eq("email", email).execute()
        if len(existing.data) > 0:
            return jsonify({"error": "Email already registered"}), 400

        # ✅ Insert user
        inserted = supabase.table("users").insert({
            "fullname": fullname,
            "email": email,
            "password": password  # later we hash it
        }).execute()

        return jsonify({"message": "User registered", "user": inserted.data}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
