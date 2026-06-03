# 🔐 LLM-Based DevSecOps Scanner

This project scans Pull Requests for security vulnerabilities using **Gemini AI** and a **Python static scanner**, integrated into GitHub Actions.

---

## How It Works

When a Pull Request is opened targeting `main`:
- The Python scanner checks the code diff for known vulnerability patterns
- Gemini AI performs a deeper contextual review of the same diff
- Both results are posted as comments directly on the PR

---

## Vulnerabilities Detected

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

## Tech Stack

- **GitHub Actions** — CI/CD pipeline automation
- **Gemini 2.5 Flash** — LLM-powered contextual code review
- **Python** — Static vulnerability pattern scanner

---

## Project Structure

- `scanner.py` — Static vulnerability scanner
- `test_github_action.py` — Sample vulnerable file for testing
- `.github/workflows/llm-int.yml` — Gemini AI security review
- `.github/workflows/Comment-git-diff.yml` — Posts PR diff as comment
- `.github/workflows/comment-on-pr.yml` — Welcome message on PR

---

## Setup

1. Fork this repository
2. Add your Gemini API key as a GitHub secret named `GOOGLE_API_KEY`
3. Open a Pull Request — the scanner runs automatically