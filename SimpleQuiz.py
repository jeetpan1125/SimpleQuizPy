# Simple Quiz Game with Categories by Jeet Panchal

import random

# Format: [Question, Options..., Correct Index] 
# if you want to edit follow the same format.
data = {
    "Geography": [
        ["What is the capital of France?", "Paris", "Delhi", "Lagos", "Rome", 1],
        ["Which is the largest ocean?", "Atlantic", "Indian", "Pacific", "Arctic", 3],
        ["Which country has the largest population?", "India", "USA", "China", "Russia", 1]
    ],
    "Math": [
        ["2 + 2 = ?", "3", "4", "5", "6", 2],
        ["What is 10 * 5?", "40", "50", "60", "70", 2],
        ["What is the square root of 64?", "6", "7", "8", "9", 3]
    ],
    "Compsci": [
        ["Which language is for web development?", "Python", "C++", "HTML", "Java", 3],
        ["What does 'CPU' stand for?", "Central Process Unit", "Control Processing Unit", "Central Processing Unit", "Computer Personal Unit", 3],
        ["Which of these is an Operating System?", "Python", "Windows", "HTML", "Java", 2]
    ]
}
print("Simple Quiz Game.\n")
print("Available Categories: Geography, Math, Compsci")

while True:
    choice = input("\nPick a category: ").strip().capitalize()
    
    if choice in data:
        questions = data[choice]
        break
    else:
        print(f"'{choice}' is not a valid category. Please try again.")

random.shuffle(questions)
score = 0

for q_list in questions:
    while True:
        question_text = q_list[0]
        option1 = q_list[1]
        option2 = q_list[2]
        option3 = q_list[3]
        option4 = q_list[4]
        correct_answer = q_list[5]

        print("\n" + question_text)
        print(f"1. {option1}")
        print(f"2. {option2}")
        print(f"3. {option3}")
        print(f"4. {option4}")

        user_guess = input("Type the number of your answer: ")

        try: 
            user_guess_number = int(user_guess)
            
            if user_guess_number < 1 or user_guess_number > 4:
                print("Invalid. Please enter a number ranging from 1 to 4 inclusive.")
                continue

            if user_guess_number == correct_answer:
                print("Correct.")
                score = score + 1
            else:
                print("Wrong answer.")
                correct_text = q_list[correct_answer]
                print("The correct answer was: " + correct_text)

            break

        except ValueError:
            print("Invalid input. Please enter a number (1-4).")
       
print("\nThank you for playing.")
print(f"Category: {choice}")
print(f"Your final score is: {score}/3\n")