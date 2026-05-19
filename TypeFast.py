import time

paragraph = "Python is a powerful and easy programming language."

print("\n===== Typing Speed Tester =====")
print("Type this sentence: ")
print(paragraph)

input("     Press Enter when you are ready...")

start_time = time.time()

typed_text = input("\nStart typing: ")

end_time = time.time()

time_taken = end_time - start_time

word_count = len(typed_text.split())

speed = (word_count / time_taken) * 60

print("\n===== Result =====")

print(f"Time Taken: {round(time_taken, 2)} seconds")

print(f"Typing Speed: {round(speed, 2)} WPM")

if typed_text == paragraph:
    print("Accuracy: 100%")
else:
    print("Accuracy: Some mistakes were made")