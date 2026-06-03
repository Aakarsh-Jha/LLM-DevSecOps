import subprocess
import re
import sys

def get_diff():
    """Fetch git diff for the current PR."""
    result = subprocess.run(["git", "diff", "origin/main...HEAD"], capture_output=True, text=True)
    return result.stdout

def scan_vulnerabilities(diff):
    findings = []

    rules = {
        "API Key":              r"['\"](AKIA|AIza|ghp_)[0-9A-Za-z]{10,}['\"]",
        "SQL Injection":        r"SELECT\s+\*\s+FROM|INSERT\s+INTO|DROP\s+TABLE",
        "Hardcoded Password":   r"password\s*=\s*['\"].+['\"]",
        "JWT Secret":           r"jwt[_\-]?secret\s*=\s*['\"].+['\"]",
        "MD5 Usage":            r"createHash\(['\"]md5['\"]\)",
        "Hardcoded Token":      r"token\s*=\s*['\"].{8,}['\"]",
        "Private Key":          r"-----BEGIN (RSA|EC|OPENSSH) PRIVATE KEY-----",
        "XSS Risk":             r"innerHTML\s*=|document\.write\s*\(",
    }

    for name, pattern in rules.items():
        matches = re.findall(pattern, diff, re.IGNORECASE)
        if matches:
            findings.append(f"{name} detected {len(matches)} time(s)")

    return findings

def main():
    diff = get_diff()

    if not diff:
        print("⚠️  No diff found. Make sure you're on a branch ahead of origin/main.")
        sys.exit(0)

    findings = scan_vulnerabilities(diff)

    if findings:
        print("⚠️  Vulnerabilities found:")
        for f in findings:
            print(f"  - {f}")
        sys.exit(1)  # Fail the pipeline if issues found
    else:
        print("✅ No vulnerabilities found.")
        sys.exit(0)

if __name__ == "__main__":
    main()