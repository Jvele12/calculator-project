# Advanced Modular Calculator by Jorge Velecela

An advanced calculator built in Python.  
---

## 🚀 Features

- **REPL Interface:** Continuous user interaction with commands such as `help`, `history`, `undo`, `redo`, `clear`, `save`, and `load`.
- **Advanced Operations:** Addition, subtraction, multiplication, division, power, and root.
- **Design Patterns Implemented:**
  - Factory Pattern (creates operations dynamically)
  - Strategy Pattern (interchangeable operation logic)
  - Observer Pattern (automatic logging and autosave)
  - Memento Pattern (undo/redo state management)
  - Facade Pattern (simplified interface through `Calculator` class)
- **Persistent History:** All calculations are stored and automatically saved/loaded via a CSV file using `pandas`.
- **Configuration Management:** Uses `.env` file and `python-dotenv` to manage autosave and history file path.
- **Full Test Coverage:** Verified with `pytest` and `pytest-cov`.
- **Continuous Integration:** GitHub Actions pipeline automatically runs all tests and enforces 100% coverage.

---

## 🛠️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Jvele12/calculator-advanced.git
   cd calculator-advanced

python -m venv venv
venv\Scripts\activate   # Windows
source venv/Scripts/activate  # Git Bash

pip install -r requirements.txt
