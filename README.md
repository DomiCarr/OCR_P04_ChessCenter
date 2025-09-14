# ♟️ ChessCenter

**ChessCenter** is a Python application designed to manage chess tournaments, including player registration, tournament creation, match results, and rankings.

---

## 📚 Table of Contents

- [Features](#-features)
- [Application Architecture](#-application-architecture)
- [Installation Guide](#-installation-guide)
- [Launch the Application](#-launch-the-application)
- [Code Quality Report (Flake8)](#-code-quality-report-flake8)
- [Built With](#-built-with)
- [Releases](#-releases)
- [Author](#-author)
- [License](#-license)

---

## 🧩 Features

- Add and list chess players
- Create and manage tournaments
- Register players to tournaments
- Start tournaments and enter match results
- Display tournament rankings
- Persist data in JSON format

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
├── env/                  # Virtual environment (excluded from version control)
├── data/                 # JSON files for players and tournaments
├── docs/                 # Documentation and project notes
├── flake8_rapport/       # Code linting reports
├── src/                  # Main application source code
│   ├── main.py           # Entry point of the application
│   ├── config.py         # Configuration settings
│   ├── controllers/      # Business logic and flow control
│   ├── models/           # Data models and domain classes
│   ├── views/            # Console-based user interfaces
```

---

## 🚀 Installation Guide

> ⚠️ **Compatibility Note**
> This project requires **Python ≥ 3.10** and **pip ≥ 23.0** to ensure full compatibility with Flake8 and its HTML reporting plugin.

> 🐧 **Note macOS/Linux**
> On Linux/Mac, the `python` command may not be available by default.
> Use `python3` instead:

Clone the repository from GitHub:

```bash
git clone https://github.com/DomiCarr/OCR_P04_ChessCenter
cd OCR_P04_ChessCenter
```

### 🛠️ Set up the virtual environment

Create and activate the virtual environment before installing packages or running the application.

Create:

```bash
python -m venv env
# If python doesn't work, use python3:
python3 -m venv env
```

Activate:

- **On macOS/Linux**
  ```bash
  source env/bin/activate
  ```

- **On Windows (CMD)**
  ```cmd
  env\Scripts\activate
  ```

- **On Windows (PowerShell)**
  ```powershell
  .\env\Scripts\Activate.ps1
  ```

> 📝 **Note (PowerShell)**
> If you get an error like
> **“running scripts is disabled on this system”**,
> open PowerShell as administrator and run:
>
> ```powershell
> Set-ExecutionPolicy RemoteSigned
> ```
>
> Then confirm with `Y` to allow local scripts to run.


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
flake8-html==0.4.3
Jinja2==3.1.6
MarkupSafe==3.0.2
mccabe==0.7.0
pycodestyle==2.14.0
pyflakes==3.4.0
Pygments==2.19.2
```

---

## ▶️ Launch the Application

```bash
cd src

python main.py
# If python doesn't work, use python3:
python3 main.py
```

---

## 🧪 Code Quality Report (Flake8)
![Flake8](https://img.shields.io/badge/code%20style-Flake8-blue)


To ensure code quality and compliance with PEP8 standards, this project uses **Flake8** with HTML reporting.

You can generate a detailed linting report by running the following command from the root of the project:

```bash
python -m flake8 src/ --format=html --htmldir=flake8_rapport
# If python doesn't work, use python3:
python3 -m flake8 src/ --format=html --htmldir=flake8_rapport
```

This will create an HTML report in the `flake8_rapport/` directory.
You can open `flake8_rapport/index.html` in your browser to review warnings, errors, and style issues.

> ⚙️ **Configuration Note**
> Flake8 is configured via a `.flake8` file located at the root of the project.
> It sets the maximum line length to 119 characters, excludes folders like `env/`, `__pycache__/`, and `flake8_rapport/`, and enables HTML output in the `flake8_rapport/` directory.

> ✅ Tip: Make sure your virtual environment is activated before running the command.

---

## 🧰 Built With

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

- **Python** — main programming language
- **MVC (Model–View–Controller)** — architectural pattern used to separate concerns between data (Model), user interface (View), and logic (Controller)
**Cross-platform compatibility** — works on 🐧 Linux, 🍎 macOS, and 🪟 Windows


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
