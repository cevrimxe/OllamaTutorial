import requests
import json
import re

# Ollama API URL
url = "http://localhost:11434/api/chat"

# User input
user_prompt = """
Please create a 3-day workout plan. For each day, include the following details:
1. The muscle group focus for the day (e.g., chest, back, legs, etc.)
2. The name of each exercise (Please do not use hyphens in the exercise names. For example, use 'Push ups' instead of 'Push-ups')
3. The number of sets and reps
4. Rest times
Please organize the program for each day as follows:

Day 1:
- Muscle Group: [Muscle Group Name]
- Exercise 1: [Exercise Name] - Sets: [X], Reps: [Y], Rest: [Z] minutes
- Exercise 2: [Exercise Name] - Sets: [X], Reps: [Y], Rest: [Z] minutes
- Exercise 3: [Exercise Name] - Sets: [X], Reps: [Y], Rest: [Z] minutes

Day 2:
- Muscle Group: [Muscle Group Name]
- Exercise 1: [Exercise Name] - Sets: [X], Reps: [Y], Rest: [Z] minutes
- Exercise 2: [Exercise Name] - Sets: [X], Reps: [Y], Rest: [Z] minutes
- Exercise 3: [Exercise Name] - Sets: [X], Reps: [Y], Rest: [Z] minutes

Day 3:
- Muscle Group: [Muscle Group Name]
- Exercise 1: [Exercise Name] - Sets: [X], Reps: [Y], Rest: [Z] minutes
- Exercise 2: [Exercise Name] - Sets: [X], Reps: [Y], Rest: [Z] minutes
- Exercise 3: [Exercise Name] - Sets: [X], Reps: [Y], Rest: [Z] minutes
"""

# Data to send to the API
payload = {
    "model": "qwen2.5",  
    "messages": [{"role": "user", "content": user_prompt}]
}

# Send request to the API
response = requests.post(url, json=payload, stream=True)

# Check the status of the response
if response.status_code == 200:
    full_text = ""
    
    print("\n\033[1;34m💬 AI Response:\033[0m")  # Blue title (for better visual in terminal)

    # Collect response data line by line
    for line in response.iter_lines(decode_unicode=True):
        if line:
            try:
                json_data = json.loads(line)
                # Check if the response is complete
                if json_data.get("done"):  # If the response is complete
                    full_text += json_data["message"]["content"]
                    print(full_text)  # Print the full response
                    break  # Exit the loop as the response is finished
                else:
                    full_text += json_data["message"]["content"]  # Accumulate the response
            except json.JSONDecodeError:
                print(f"\n⚠️ Error: {line}")  # In case of JSON decode error

    # Use regex to directly extract exercise names after "Exercise" (without symbols)
    exercise_names = re.findall(r"Exercise \d+: ([\w\s]+)", full_text)

    # Store exercises in variables (Example: Day 1, Exercise 1, etc.)
    day1_exercise1 = exercise_names[0] if len(exercise_names) > 0 else None
    day1_exercise2 = exercise_names[1] if len(exercise_names) > 1 else None
    day1_exercise3 = exercise_names[2] if len(exercise_names) > 2 else None
    
    day2_exercise1 = exercise_names[3] if len(exercise_names) > 3 else None
    day2_exercise2 = exercise_names[4] if len(exercise_names) > 4 else None
    day2_exercise3 = exercise_names[5] if len(exercise_names) > 5 else None
    
    day3_exercise1 = exercise_names[6] if len(exercise_names) > 6 else None
    day3_exercise2 = exercise_names[7] if len(exercise_names) > 7 else None
    day3_exercise3 = exercise_names[8] if len(exercise_names) > 8 else None


    print("\n----------------------------------\n")

    # Print the exercises for each day
    print("\nExercises for Day 1:")
    print(f"Exercise 1: {day1_exercise1}")
    print(f"Exercise 2: {day1_exercise2}")
    print(f"Exercise 3: {day1_exercise3}")

    print("\nExercises for Day 2:")
    print(f"Exercise 1: {day2_exercise1}")
    print(f"Exercise 2: {day2_exercise2}")
    print(f"Exercise 3: {day2_exercise3}")

    print("\nExercises for Day 3:")
    print(f"Exercise 1: {day3_exercise1}")
    print(f"Exercise 2: {day3_exercise2}")
    print(f"Exercise 3: {day3_exercise3}")

else:
    print(f"\n❌ Error: {response.status_code}")
    print(response.text)
