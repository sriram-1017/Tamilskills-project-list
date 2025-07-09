import re
import math
import random
import string
from pathlib import Path

BLACKLIST_PATH = Path("utils/blacklist.txt")

if BLACKLIST_PATH.exists():
    with open(BLACKLIST_PATH, "r", encoding="utf-8") as f:
        BLACKLIST = set(line.strip().lower() for line in f)
else:
    BLACKLIST = set()

def calculate_entropy(password):
    charset = 0
    if any(c.islower() for c in password): charset += 26
    if any(c.isupper() for c in password): charset += 26
    if any(c.isdigit() for c in password): charset += 10
    if any(c in "!@#$%^&*()-_+=[]{}|;:,.<>?/" for c in password): charset += 32
    return round(len(password) * math.log2(charset), 2) if charset else 0.0

def is_blacklisted(password):
    return password.lower() in BLACKLIST

def generate_suggestions(result):
    suggestions = []
    if result["length"] < 12:
        suggestions.append("Use at least 12–16 characters.")
    if not result["has_upper"]:
        suggestions.append("Add uppercase letters (A–Z).")
    if not result["has_lower"]:
        suggestions.append("Include lowercase letters (a–z).")
    if not result["has_digit"]:
        suggestions.append("Include numbers (0–9).")
    if not result["has_special"]:
        suggestions.append("Add symbols like @, #, $, %.")
    if result["is_blacklisted"]:
        suggestions.append("Avoid common or leaked passwords.")
    return suggestions

def generate_example_password(base):
    new = base + ''.join(random.choices(string.ascii_uppercase + string.digits + "!@#", k=5))
    return new

def evaluate_password(password):
    result = {
        "length": len(password),
        "has_upper": bool(re.search(r"[A-Z]", password)),
        "has_lower": bool(re.search(r"[a-z]", password)),
        "has_digit": bool(re.search(r"\d", password)),
        "has_special": bool(re.search(r"[^a-zA-Z0-9]", password)),
        "entropy": calculate_entropy(password),
        "is_blacklisted": is_blacklisted(password)
    }

    score = sum([
        result["has_upper"],
        result["has_lower"],
        result["has_digit"],
        result["has_special"],
        result["length"] >= 12,
        not result["is_blacklisted"]
    ])

    if score <= 2:
        result["strength"] = "Weak"
    elif score <= 4:
        result["strength"] = "Moderate"
    else:
        result["strength"] = "Strong"

    result["suggestions"] = generate_suggestions(result)
    return result
