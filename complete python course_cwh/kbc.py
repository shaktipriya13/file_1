import random

# Define the list of questions and answers as tuples (question, correct_answer, prize_amount)
questions = [
    ("What is the capital of France?", "Paris", 1000),
    ("Which planet is known as the Red Planet?", "Mars", 2000),
    ("What is the largest mammal in the world?", "Blue whale", 3000),
    ("What is the currency of Japan?", "Yen", 5000),
    ("Who wrote the play 'Romeo and Juliet'?", "William Shakespeare", 10000),
    ("Which gas do plants absorb from the atmosphere?", "Carbon dioxide", 20000),
    ("Which element has the chemical symbol 'H'?", "Hydrogen", 50000),
    ("What is the largest organ in the human body?", "Skin", 100000),
    ("How many continents are there on Earth?", "7", 500000),
    ("What is the capital of Australia?", "Canberra", 1000000)
]

def play_game():
    total_prize = 0
    for i, (question, correct_answer, prize_amount) in enumerate(questions):
        print(f"Question {i + 1}: {question}")
        user_answer = input("Your answer: ").strip()
        
        if user_answer.lower() == correct_answer.lower():
            total_prize += prize_amount
            print(f"Correct! You won ${prize_amount}")
        else:
            print(f"Sorry, the correct answer was '{correct_answer}'. You won ${total_prize}")
            break
    
    print(f"Congratulations! You are taking home ${total_prize}")

# Start the game
print("Welcome to Who Wants to Be a Millionaire?")
print("You'll be asked a series of questions. Answer correctly to win the prize.")
play_game()
