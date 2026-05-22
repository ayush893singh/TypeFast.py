# TypeFast
A simple Python Typing Speed Tester project that calculates typing speed and accuracy.

# Features
- Typing speed calculation
- Accuracy checking
- Time tracking
- Beginner-friendly Python project
- Simple terminal-based interface

# Technologies Used
- Python
- time module

# Concepts Used
This project uses:-

- Variables
- Input and Output
- Strings
- Conditions
- Functions
- Time module
- Word counting
- Speed calculation

# Installation
1. Install Python from:
https://www.python.org/

2. Download the project files.

3. Open terminal or command prompt.

4. Run the file.

# How to Run
python main.py

# How It Works
1. The program shows a sentence.
2. User presses Enter to start.
3. Timer starts automatically.
4. User types the sentence.
5. Timer stops after typing.
6. Program calculates:
   - Time Taken
   - Typing Speed (WPM)
   - Accuracy

# Future Improvements
- Multiple paragraphs
- Accuracy percentage
- Difficulty levels
- GUI version
- Leaderboard system
  
# Example Output
```
===== Typing Speed Tester =====

Type this sentence:

Python is a powerful and easy programming language.

Press Enter when you are ready...

Start typing:
Python is a powerful and easy programming language.

===== Result =====

Time Taken: 10.45 seconds
Typing Speed: 45.93 WPM
Accuracy: 100%
```
# Conditions Used

```python
if typed_text == paragraph:
    print("Accuracy: 100%")
else:
    print("Accuracy: Some mistakes were made")
```

This condition checks whether the typed sentence matches the original sentence.

---

# Formula Used

```python
speed = (word_count / time_taken) * 60
```

This formula calculates typing speed in Words Per Minute (WPM).

---
# Author
https://github.com/ayush893singh
