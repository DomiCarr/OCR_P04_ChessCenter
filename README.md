# ♟️ ChessCenter

**ChessCenter** is a Python application designed to manage chess tournaments, including player registration, tournament creation, match results, and rankings.

---

## 🧠 Application Architecture

ChessCenter is organized using a clean modular architecture based on the Model–View–Controller (MVC) pattern.
Each component has its own dedicated folder, making the codebase easy to navigate and maintain.

- **Models** handle the core data structures (players, tournaments, matches, etc.)
- **Views** manage user interaction via the console
- **Controllers** coordinate logic between models and views
- **Data** stores persistent tournament and player information in JSON format

Here’s the overall project layout:

```
ChessCenter/
├── README.md
├── requirements.txt
├── data/                 # JSON files for players and tournaments
├── docs/                 # Documentation and project notes
├── flake8_rapport/       # Code linting reports
├── src/                  # Main application source code
│   ├── main.py           # Entry point of the application
│   ├── config.py         # Configuration settings
│   ├── env/              # Virtual environment (excluded from version control)
│   ├── controllers/      # Business logic and flow control
│   ├── models/           # Data models and domain classes
│   ├── views/            # Console-based user interfaces
```

---

## 🚀 Installation Guide

Clone the repository from GitHub:

```bash
git clone https://github.com/DomiCarr/OCR_P04_ChessCenter
cd OCR_P04_ChessCenter
```

### 🛠️ Set up the virtual environment

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 📦 Install dependencies

```bash
pip install -r requirements.txt
```

### ✅ Verify installation

Run the following to confirm packages are installed:

```bash
pip freeze
```

Expected output includes:

```text
flake8==7.3.0
mccabe==0.7.0
pycodestyle==2.14.0
pyflakes==3.4.0
```

---

## ▶️ Launch the Application

```bash
cd src
python ChessCenter.py
```

---

## 🧰 Built With

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

---

## 📦 Releases

- **Version 1.0** — Initial release

---

## 👤 Author

**Dominique Carrasco**
GitHub: [@DomiCarr](https://github.com/DomiCarr)

---

## 📄 License

This project is licensed under the [OpenClassrooms Terms & Conditions](https://openclassrooms.com/fr/policies/terms-conditions)
