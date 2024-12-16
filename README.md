
# Django Quiz App

This is a simple Django web application for a quiz. It includes basic functionality for starting a quiz, fetching random questions, and submitting answers.

## Assumptions
1. The user is the only one interacting with the quiz.
2. There are pre-existing questions in the database.
3. The quiz will display a random question and allow the user to submit an answer.
4. The quiz shows the total score after completing 10 questions.

## How to run
1. Clone the repository.
2. Install the dependencies: `pip install -r requirements.txt`.
3. Run migrations: `python manage.py migrate`.
4. Start the development server: `python manage.py runserver`.
5. Visit `http://127.0.0.1:8000/quiz/` to start the quiz.

