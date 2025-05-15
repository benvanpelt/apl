# -*- coding: utf-8 -*-
"""
Created on Thu May 15 09:18:06 2025

@author: BenVanPelt
"""

from flask import Flask, jsonify, request
import requests
import os

app = Flask(__name__)

SUPABASE_URL = "https://hdbfowhiscynicqzqmpn.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhkYmZvd2hpc2N5bmljcXpxbXBuIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDcyNDE5MDgsImV4cCI6MjA2MjgxNzkwOH0.UKOGJ64EQB1IrGCmPw6jaJHmxdb678Gbnfpca-Zp_YY"

@app.route ("/data", methods = ["GET"])
def get_data():
        headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}"
    }
    url = f"{SUPABASE_URL}/rest/v1/apl_drops"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run (debug=True, host = "0.0.0.0", port = 5000)
