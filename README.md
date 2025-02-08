# Finance with Python | GHW AI/ML Week 2025

## Session 1

### Setup Python Environment

0. Ensure Python is installed on your system - [https://www.python.org/downloads/](https://www.python.org/downloads/)
1. Open Terminal in VSCode
2. Ensure you're in the project folder `<path-to-finance-with-python> folder`
3. Create Virtual Environment: [https://docs.python.org/3/library/venv.html](https://docs.python.org/3/library/venv.html)
    - `python -m venv finance_env`
4. Activate Virtual Environment
    - Mac/Linux: `source finance_env/bin/activate`
    - Windows: `.\finance_env\Scripts\activate`
5. Verify Activation
    - Mac/Linux: `which python`
    - Windows: `where python`
6. Install required packages
    - `pip install numpy pandas matplotlib yfinance mplfinance plotly jupyter`
7. Create requirements.txt file
    - `pip freeze > requirements.txt`
    - To install from requirements.txt file: `pip install -r requirements.txt`
8. To Deactivate virtual environment (when needed)
    - Mac/Linux/Windows: `deactivate`
9. VSCode Integration
    - Press Ctrl/Cmd + Shift + P
    - Type: "Python: Select Interpreter"
    - Choose the interpreter: finance_env

### Open Jupyter Notebook

1. Open Jupyter Notebook:
    - In Terminal: `jupyter notebook`
    - This should open in browser
2. Create a new Python3 notebook in the desired folder
