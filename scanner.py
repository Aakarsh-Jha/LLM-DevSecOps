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

    # Create findings file for Gemini to read later
    with open("static_findings.txt", "w") as f:
        if not diff:
            f.write("No diff found to scan.")
            sys.exit(0)

        findings = scan_vulnerabilities(diff)

        if findings:
            f.write("⚠️ Static Scanner Rule-Based Matches:\n")
            for finding in findings:
                f.write(f"  - {finding}\n")
        else:
            f.write("✅ Static Scanner found no rule-based vulnerabilities.\n")

    print("✅ Static scan complete. Results passed to temporary buffer.")
    sys.exit(0)  # Always pass so Gemini can act as the contextual layer

if __name__ == "__main__":
    main()