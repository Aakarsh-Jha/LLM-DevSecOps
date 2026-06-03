# test_github_action.py
# Intentionally vulnerable sample file for testing the DevSecOps scanner

# ⚠️ Hardcoded API Key (CWE-798)
const HARDCODED_API_KEY = "AKIA_FAKE_KEY_1234567890";

# ⚠️ Weak JWT Secret (CWE-321)
JWT_SECRET = "supersecret_jwt_key"

# ⚠️ Hardcoded Password (CWE-259)
password = "admin123"

# ⚠️ SQL Injection risk (CWE-89)
# query = "SELECT * FROM users WHERE id=" + user_input

# ⚠️ MD5 weak hashing (CWE-327)
# crypto.createHash('md5').update(pw).digest('hex')

# ⚠️ XSS Risk (CWE-79)
# element.innerHTML = userInput
