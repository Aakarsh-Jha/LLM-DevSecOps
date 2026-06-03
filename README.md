# 🔐 LLM-Based DevSecOps Scanner

Automatically scans Pull Requests for security vulnerabilities using **Gemini AI** + **static analysis**, integrated directly into the GitHub CI/CD pipeline.

---

## 🚀 How It Works

1. Developer opens a Pull Request targeting `main`
2. GitHub Actions triggers automatically
3. Python static scanner checks the diff for known patterns
4. Gemini AI performs deep contextual analysis
5. Vulnerabilities are reported as PR comments instantly

---

## 🔍 Detected Vulnerabilities

| Vulnerability | Severity | CWE |
|---|---|---|
| Hardcoded API Keys | CRITICAL | CWE-798 |
| SQL Injection | HIGH | CWE-89 |
| Hardcoded Passwords | HIGH | CWE-259 |
| Weak JWT Secrets | HIGH | CWE-321 |
| MD5 Weak Hashing | MEDIUM | CWE-327 |
| XSS Risk | HIGH | CWE-79 |
| Hardcoded Tokens | MEDIUM | CWE-798 |
| Exposed Private Keys | CRITICAL | CWE-321 |

---

## 🛠️ Tech Stack

- **GitHub Actions** — CI/CD pipeline automation
- **Gemini 2.5 Flash** — LLM-powered contextual code review
- **Python** — Static vulnerability pattern scanner

---

## 📁 Project Structure
├── scanner.py               # Static vulnerability scanner
├── test_github_action.py    # Sample vulnerable file for testing
└── .github/workflows/
├── llm-int.yml          # Gemini AI security review
├── Comment-git-diff.yml # Posts PR diff as comment
└── comment-on-pr.yml    # Welcome message on PR
---

## ⚙️ Setup

1. Fork this repository
2. Add your Gemini API key as a GitHub secret named `GOOGLE_API_KEY`
3. Open a Pull Request — the scanner runs automatically