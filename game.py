import time
import random

passages = [
    "In a small village, there lived a boy named Jack.",
    "Jack had a pet dog named Rex.",
    "Rex was the smartest dog in the village.",
    "Jack loved to take Rex for a walk in the park.",
    "In the park, they met a lot of people, and Rex would always greet them by wagging his tail.",
    "One day, a thunderstorm began, and everyone in the park ran to the nearest shelter.",
    "Except for Jack and Rex, who had been to the park so many times, knew exactly where the nearest shelter was.",
    "The two of them snuggled inside the shelter and watched the storm pass by.",
    "When the rain finally stopped, they came out and continued their walk in the park.",
    "Jack and Rex had so much fun that day, they decided to become the park's best friends.",
]

def typing_speed_test(text, wpm):
    start_time = time.time()
    user_input = input(f"Type the passage below ({wpm} WPM):\n\n{text}\n\n")
    end_time = time.time()

    user_words = len(user_input.split())
    correct_words = len(text.split())

    typing_speed = correct_words / (end_time - start_time)
    typing_speed_corrected = correct_words / ((end_time - start_time) / 60) # in words per minute

    if user_input == text:
        accuracy = 100
    else:
        accuracy = (correct_words / user_words) * 100

    return {
        "Typing Speed (words per minute)": typing_speed_corrected,
        "Accuracy (percent)": accuracy,
    }

def start_game():
    print("\nWelcome to the Writing Speed Game!")
    passage = random.choice(passages)
    print("\nType the passage below as fast as you can:\n\n")
    print(passage)
    print("\n")

    wpm = int(input("Enter your typing speed in words per minute (WPM): "))

    results = typing_speed_test(passage, wpm)

    print(f"\nTyping Speed (WPM): {results['Typing Speed (words per minute)']}")
    print(f"Accuracy (percent): {results['Accuracy (percent)']}")

    play_again = input("\nWould you like to play again? (yes/no): ")

    if play_again.lower() == "yes":
        start_game()
    else:
        print("\nThank you for playing! Have a great day!")

start_game()
