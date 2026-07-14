# Web-Based Interactive Quiz
A category-based interactive quiz web application. I took my original Python command-line quiz and re-engineered it into a full-stack web app with a visual user interface and a separate backend server.
This is my 1st full-stack Python and JavaScript project for GitHub.

## Features
- Modern Web Interface: A clean, responsive webpage to play the quiz instead of running it in a text-based terminal.
- FastAPI Backend: A lightweight Python web server that hosts the quiz data, manages session states, and serves questions securely.
- Dynamic Frontend: Uses HTML, CSS, and JavaScript (Fetch API) to load questions and check answers instantly without reloading the page.
- Input Security: The correct answers are hidden on the server so players can't cheat by looking at the website's source code.

## How to Run
To run this full-stack app locally, you need to start the backend server first, then open the frontend webpage.
1. Open your terminal and ensure your virtual enviornment is active (source .venv/bin/activate)
2. Start the FastAPI server using Uvicorn (uvicorn SimpleQuiz:app --reload)
3. Locate the index.html file in your folder explorer and double-click it to open the webpage.

## Files
- SimpleQuiz.py – main program
- index.html - frontend user interface (HTML, CSS, JavaScript)
- .gitignore – ignores system files
