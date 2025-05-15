# -*- coding: utf-8 -*-
"""
Created on Thu May 15 09:18:06 2025

@author: BenVanPelt
"""

from flask import Flask, jsonify, request
from supabase import create_client, Client
import os

app = Flask(__name__)

url = os.environ.get("https://hdbfowhiscynicqzqmpn.supabase.co")
key = os.environ.get("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhkYmZvd2hpc2N5bmljcXpxbXBuIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDcyNDE5MDgsImV4cCI6MjA2MjgxNzkwOH0.UKOGJ64EQB1IrGCmPw6jaJHmxdb678Gbnfpca-Zp_YY")

supabase: Client = create_client(url, key)

@app.route ("/data", methods = ["GET"])
def get_data():
    try:
        response = supabase.table("apl_drops").select("*").execute()
        return jsonify(response.data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run (debug=True, host = "0.0.0.0", port = 5000)


