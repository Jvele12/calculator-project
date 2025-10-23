# 🧮 Advanced Modular Calculator  
### by Jorge Velecela  

An advanced, pattern-driven calculator built in **Python** with robust error handling, history management, undo/redo, and continuous integration.  

---

## 🚀 Features

- **Interactive REPL Interface**  
  Perform calculations continuously using commands like:
add 2 3
undo
redo
help
exit

markdown
Copy code
- **Advanced Arithmetic Operations**
- `add`, `subtract`, `multiply`, `divide`
- `power`, `root`, `modulus`
- `int_divide`, `percent`, `abs_diff`
- **Design Patterns Implemented**
- 🏭 **Factory Pattern** – dynamic operation creation  
- 🔁 **Memento Pattern** – supports `undo` / `redo`  
- 👁️ **Observer Pattern** – automatic logging and auto-save  
- ⚙️ **Strategy Pattern** – interchangeable operation logic
- 🌈 **Coloroma**
- **Persistent History**
- Automatically saves to CSV using **pandas**  
- Undo and redo supported through Memento design
- **Logging System**
- Each operation logged to file via Python’s `logging` module
- **Configurable via `.env`**
- Easy customization of file paths, precision, and limits
- **Comprehensive Testing**
- 90 %+ coverage enforced with `pytest` + `pytest-cov`
- **Continuous Integration**
- GitHub Actions automatically run tests and enforce coverage

---

## 🛠️ Installation & Setup

1. **Clone the repository**
2. 
 git clone https://github.com/Jvele12/calculator-project.git
 cd calculator-project
Create & activate a virtual environment

python -m venv venv
venv\Scripts\activate       # Windows
Install dependencies

pip install -r requirements.txt
Create a .env file:

env
CALCULATOR_LOG_DIR=logs
CALCULATOR_HISTORY_DIR=history
CALCULATOR_MAX_HISTORY_SIZE=100
CALCULATOR_AUTO_SAVE=true
CALCULATOR_PRECISION=4
CALCULATOR_MAX_INPUT_VALUE=100000
CALCULATOR_DEFAULT_ENCODING=utf-8

▶️ Usage
Run the calculator REPL:

python -m app.calculator
Example session:
Welcome to the Advanced Calculator! Type 'help' for commands.

>> add 5 3
✅ add(5.0, 3.0) = 8.0
>> power 2 4
✅ power(2.0, 4.0) = 16.0
>> undo
↩️  Undid last operation.
>> redo
↪️  Redid last undone operation.
>> exit
👋 Goodbye!

🧩 Structure
project_root/
├── app/
│   ├── calculator.py
│   ├── calculation.py
│   ├── calculator_config.py
│   ├── calculator_memento.py
│   ├── history.py
│   ├── operations.py
│   ├── logger.py
│   ├── input_validators.py
│   ├── exceptions.py
│   └── __init__.py
├── tests/
│   ├── test_calculator.py
│   ├── test_operations.py
│   ├── test_history.py
│   ├── test_input_validators.py
│   ├── test_memento.py
│   └── __init__.py
├── requirements.txt
├── .env
├── README.md
└── .github/
    └── workflows/
        └── python-app.yml
🧪 Testing
Run tests with coverage:


pytest --cov=app --cov-report=term-missing
GitHub Actions will automatically:

Install dependencies

Run all tests

Fail the workflow if coverage < 90 %

🧠 Design Pattern Summary
Pattern	Purpose	Implemented In
Factory	Create operations dynamically	operation_factory.py
Strategy	Encapsulate operation logic	operations.py
Memento	Undo / redo calculator history	calculator_memento.py
Observer	Log and auto-save events	logger.py, history.py
Facade	Simplified interface to subsystems	calculator.py

💡 Author
Jorge Velecela

