#Step 1: Have a dictionary that stores the questions and answers 
#Step 2: Have a variable that tracks the score 
#Step 3: loop through the dictionary using key-value pairs 
#Step 4: Display each question to the user and allow them to answer 
#Step 5: Tell them if they are right or wrong
#Step 6 Show final score when quiz is complete

questions = {
    "Which famous play features a character named Romeo?": "Romeo and Juliet",
    "What is the only planet that rotates on its side?": "Uranus",
    "What is the official animal of Scotland?": "Unicorn",
    "What fruit is known as the “king of fruits” and is banned in many hotels and public transportation in Southeast Asia due to its strong smell?": "Durian"
}

score = 0

for q in questions.keys():
    answer = input(q)
    if answer == questions[q]:
        print("Great job! you are correct!")
        score += 25
    else:
        print(f"Sorry, that is incorrect. The correct answer is {questions[q]}")

print(f"Your score is: {score}%!")