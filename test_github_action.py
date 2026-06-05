# test_github_action.py
# Intentionally vulnerable sample file for pipeline verification

import sqlite3
import hashlib

# ⚠️ Hardcoded Mock Key (CWE-798)
FAKE_API_KEY = "AKIA_MOCK_VAL_1234567890"

# ⚠️ Weak JWT Secret Configuration (CWE-321)
JWT_SECRET_KEY = "supersecret_jwt_key"

def get_user_data(user_id):
    # ⚠️ SQL Injection Vulnerability (CWE-89)
    conn = sqlite3.connect("app_database.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE id = '" + str(user_id) + "'"
    cursor.execute(query)
    return cursor.fetchall()

def insecure_password_hash(password):
    # ⚠️ Cryptographically Broken Hashing Algorithm (CWE-327)
    return hashlib.md5(password.encode()).hexdigest()