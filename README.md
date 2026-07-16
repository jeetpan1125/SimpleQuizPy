# Web-Based Interactive Quiz
A category-based interactive quiz web application. I took my original Python command-line quiz and re-engineered it into a full-stack web app with a visual user interface and a separate backend server.
This is my 1st full-stack Python and JavaScript project for GitHub.

## Features
- Modern Web Interface: A clean, responsive webpage to play the quiz instead of running it in a text-based terminal.
- FastAPI Backend: A lightweight Python web server that hosts the quiz data, manages session states, and serves questions securely.
- Dynamic Frontend: Uses HTML, CSS, and JavaScript (Fetch API) to load questions and check answers instantly without reloading the page.
- Input Security: The correct answers are hidden on the server so players can't cheat by looking at the website's source code.

## Clone or Download the Project
Open your terminal and run: 
```bash
git clone [https://github.com/jeetpan1125/SimpleQuizPy.git](https://github.com/jeetpan1125/SimpleQuizPy.git)
cd SimpleQuizPy
```

## How to Run
To run this full-stack app locally, you need to start the backend server first, then open the frontend webpage.
1. Create a fresh virtual environment (python3 -m venv .venv)
2. Activate the virtual enviornment (source .venv/bin/activate)
3. Install the required packages (pip install -r requirements.txt)
4. Start the backend server (uvicorn SimpleQuiz:app --reload)
5. Locate the index.html file in your folder explorer and double-click it to open the webpage.

## Files
- SimpleQuiz.py – main program
- index.html - frontend user interface (HTML, CSS, JavaScript)
- requirements.txt - lists all the required python packages
- .gitignore – ignores system files
