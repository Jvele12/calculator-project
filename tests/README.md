# Calculator CLI Project by Jorge Velecela

A simple command-line calculator built in Python.  
Supports addition, subtraction, multiplication, and division with full test coverage and continuous integration via GitHub Actions.

## Features
- REPL interface for continuous user interaction
- Handles invalid inputs and divide-by-zero errors gracefully
- Fully tested with pytest and 100% coverage
- CI pipeline that enforces passing tests and coverage

## Setup Instructions

1. Clone the repository:
   git clone https://github.com/Jvele12/calculator-ci.git
   cd calculator-ci

2. Create a virtual environment with
    python -m venv .venv
    .venv\Scripts\activate  

3. Install dependencies 
    pip install -r requirements.txt

## Run program 
    python -m src.main

## Pytest
    use pytest