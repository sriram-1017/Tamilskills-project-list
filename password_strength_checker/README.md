
----
# 🔐 Password Strength Checker

This is a professional-grade Password Strength Checker built with **Python** and **Tkinter**.
## ✅ Features

- GUI-based interface using Tkinter
- Real-time password strength evaluation
- Entropy calculation
- Common password blacklist detection
- Suggestions for improvement
- Example strong password generator
- Password visibility toggle
- Color-coded feedback (Weak, Moderate, Strong)

---
## 💻 Technologies Used

- Python 3.x
- Tkinter (GUI)
- Regex for pattern matching
- NLTK for dictionary word detection
- Custom blacklist for known weak passwords

---
## 📁 Project Structure

```css
password_strength_checker/
├── GUI/
│   └── main.py             # Tkinter UI
|
|── WEB/
│   └── Templates/index.html 
│   └── app.py             # Web based 
|
├── utils/
│   ├── checker.py          # Core password logic & NLTK
│   └── blacklist.txt       # Common leaked passwords
|
├── requirements.txt        # Required packages
└── README.md               # Documentation
```


---
## 🧪 How It Works

>When a user enters a password:
- It is evaluated using rules (length, complexity, special characters, blacklist).
- Entropy is calculated to measure randomness.
- Strength is categorized as **Weak**, **Moderate**, or **Strong**.
- Suggestions are shown to help create a stronger password.
- A sample strong version is generated (if the password is weak).

---
## 📦 Installation

1. Clone the repo or download the ZIP:

```
git clone https://github.com/your-repo/password_strength_checker.git
```

2. Run the app:

```
python ./GUI/main.py
```

3. Run the web:

```
python ./WEB/main.py
```

---
## 📄 License

This project is open-source and free to use.

---

  
Built with ❤️ by [SRIRAM]