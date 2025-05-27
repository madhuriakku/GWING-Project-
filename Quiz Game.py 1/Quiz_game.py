import time

# 10 quiz questions
quiz = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "Which language is used for web development?",
        "options": ["A. Python", "B. JavaScript", "C. C++", "D. Java"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'Macbeth'?",
        "options": ["A. Dickens", "B. Chaucer", "C. Austen", "D. Shakespeare"],
        "answer": "D"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["A. Central Processing Unit", "B. Computer Processing Unit", "C. Control Program Unit", "D. Central Power Unit"],
        "answer": "A"
    },
    {
        "question": "Which one is a programming language?",
        "options": ["A. HTML", "B. CSS", "C. Python", "D. Excel"],
        "answer": "C"
    },
    {
        "question": "What is the value of Pi (approx)?",
        "options": ["A. 2.14", "B. 3.14", "C. 4.14", "D. 5.14"],
        "answer": "B"
    },
    {
        "question": "Which is the largest planet in our Solar System?",
        "options": ["A. Earth", "B. Saturn", "C. Jupiter", "D. Mars"],
        "answer": "C"
    },
    {
        "question": "Which company developed the Windows OS?",
        "options": ["A. Apple", "B. Google", "C. Microsoft", "D. Intel"],
        "answer": "C"
    },
    {
        "question": "Which protocol is used to access web pages?",
        "options": ["A. FTP", "B. SMTP", "C. HTTP", "D. IP"],
        "answer": "C"
    },
    {
        "question": "What does RAM stand for?",
        "options": ["A. Read Access Memory", "B. Random Access Memory", "C. Remote Access Mode", "D. Run Access Module"],
        "answer": "B"
    }
]

# 💬 Starting Messages
print("🎮 Welcome to my Computer Quiz!")
play = input("Do you want to play the game? (yes/no): ").lower()

if play != "yes":
    print("❌ No problem! Maybe next time. Goodbye! 👋")
    exit()
else:
    print("✅ Great! Let's start the game!")

# Get user name
name = input("\nEnter your name: ")

# Countdown
print("\nStarting the quiz in...")
for i in range(3, 0, -1):
    print(f"{i}...")
    time.sleep(1)

print("🚀 Go!\n")

score = 0

# 🧠 Quiz Loop (No random, fixed order)
for index, q in enumerate(quiz):
    print(f"\nQuestion {index + 1}: {q['question']}")
    for option in q["options"]:
        print(option)

    start = time.time()
    answer = input("Your answer (A/B/C/D): ").upper()
    elapsed = time.time() - start

    if elapsed > 5:
        print("⏱ Time's up! You took too long.")
        continue

    if answer == q["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer was {q['answer']}")

# 🎉 Quiz Finished
print("\n🎉 Quiz Completed!")
print(f"{name}, your final score is: {score}/{len(quiz)}")

# Feedback
if score == len(quiz):
    print("🏆 Perfect score! You're a quiz master!")
elif score >= 7:
    print("👏 Great job!")
elif score >= 4:
    print("🙂 Not bad, but you can do better!")
else:
    print("😅 Keep practicing!")

# 💾 Save Score
with open("quiz_scores.txt", "a") as file:
    file.write(f"{name}: {score}/{len(quiz)}\n")

print("📁 Your score has been saved to 'quiz_scores.txt'")
