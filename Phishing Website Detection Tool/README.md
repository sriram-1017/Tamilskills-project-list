
---  
## Problem Statement: 

-  Phishing websites trick users into entering personal data, leading to identity theft and fraud.

---
## Objective: 

> Develop a Python-based tool to detect phishing URLs using:

- **Rule-based heuristics** (e.g., IP in URL, long domains, suspicious TLDs)
    
- **Machine Learning** (trained on legitimate vs. phishing URL datasets)

The tool should flag malicious URLs and help users make safer browsing decisions.

---
## Requirements: 

- Python URL dataset (legitimate & phishing) 
- Scikit-learn (for ML version) 
- Pandas
- Regex (for rule-based version) 
- Tkinter (optional GUI)

---
## Expected Outcome: 

A lightweight tool that flags suspicious URLs and helps users avoid phishing attacks. 

## Working Conditions ✅

1. **Run GUI Automatically** if no URL is passed:

```sh
python phish_detect.py
```

2. **Train the ML model**:

```sh
python phish_detect.py --ml-train dataset.csv --ml-model ml_model.pkl
```

3. **Test a URL (Rule-Based):**

```sh
python phish_detect.py --rule http://free-voucher.store
```

4. **Test a URL (ML-Based)**:

```sh
python phish_detect.py http://secure-login.bank.com
```