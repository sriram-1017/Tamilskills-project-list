import re
import sys
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# === Rule-Based Heuristic Checks ===

def rule_based_check(url):
    flags = {
        'has_ip': bool(re.search(r'http[s]?://\d+\.\d+\.\d+\.\d+', url)),
        'has_at': '@' in url,
        'is_long': len(url) > 75,
        'bad_tld': url.lower().endswith(('.zip', '.review', '.country', '.kim', '.gq', '.men')),
        'too_many_subdomains': re.sub(r'http[s]?://', '', url).split('/')[0].count('.') > 3
    }
    score = sum(flags.values())
    return flags, score >= 2

# === ML Pipeline ===

def load_dataset(path):
    df = pd.read_csv(path)
    X = df['url'].values
    y = df['label'].map({'legitimate': 0, 'phishing': 1}).values
    return X, y

def train_model(X, y, save_path):
    vec = TfidfVectorizer(analyzer='char_wb', ngram_range=(3, 5))
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    X_train_vec = vec.fit_transform(X_train)
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train_vec, y_train)
    print("ML model accuracy:", accuracy_score(y_test, model.predict(vec.transform(X_test))))
    print(classification_report(y_test, model.predict(vec.transform(X_test))))
    joblib.dump((vec, model), save_path)

def predict_ml(url, model_path):
    vec, model = joblib.load(model_path)
    X_vec = vec.transform([url])
    return bool(model.predict(X_vec)[0])

# === GUI (Tkinter) ===
try:
    import tkinter as tk
    from tkinter import messagebox
    GUI_AVAILABLE = True
except ImportError:
    GUI_AVAILABLE = False

def run_gui(model_path):
    class App:
        def __init__(self, root, model):
            self.model = model
            root.title("Phishing URL Detector")
            tk.Label(root, text="Enter URL:").pack()
            self.entry = tk.Entry(root, width=60)
            self.entry.pack(pady=5)
            tk.Button(root, text="Check (Rule-Based)", command=self.check_rule).pack(pady=2)
            tk.Button(root, text="Check (ML-Based)", command=self.check_ml).pack(pady=2)

        def check_rule(self):
            url = self.entry.get()
            flags, result = rule_based_check(url)
            verdict = "Phishing" if result else "Legitimate"
            messagebox.showinfo("Rule-Based Check", f"Flags: {flags}\nResult: {verdict}")

        def check_ml(self):
            url = self.entry.get()
            result = predict_ml(url, self.model)
            verdict = "Phishing" if result else "Legitimate"
            messagebox.showinfo("ML Check", f"Result: {verdict}")

    root = tk.Tk()
    App(root, model_path)
    root.mainloop()

# === CLI Logic ===
def cli():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--ml-train", metavar="CSV", help="Train ML model on dataset")
    parser.add_argument("--ml-model", metavar="MODEL", default="ml_model.pkl", help="Path to model")
    parser.add_argument("--rule", action="store_true", help="Use rule-based detection")
    parser.add_argument("url", nargs="?", help="URL to test")
    args = parser.parse_args()

    if args.ml_train:
        X, y = load_dataset(args.ml_train)
        train_model(X, y, args.ml_model)
        return

    if args.url:
        if args.rule:
            flags, verdict = rule_based_check(args.url)
            print(f"Flags: {flags}\nResult: {'Phishing' if verdict else 'Legitimate'}")
        else:
            print("Result:", "Phishing" if predict_ml(args.url, args.ml_model) else "Legitimate")
    else:
        if GUI_AVAILABLE:
            run_gui(args.ml_model)
        else:
            print("Tkinter not available and no URL provided. Use CLI or install Tkinter.")

if __name__ == "__main__":
    cli()
