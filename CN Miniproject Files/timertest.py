# import tkinter as tk
# import time

# def update_timer():
    # global remaining_time
    # remaining_time=6
    
    # for i in range(6,0,-1):
    #     print(i)
    #     timer_label.config(text=f"Time Remaining: {i} seconds")
    #     time.sleep(1)
    # print("time up")
        

    # if remaining_time > 0:
    #     remaining_time -= 1
    #     timer_label.config(text=f"Time Remaining: {remaining_time} seconds")
    #     root.after(1000, update_timer)
    # else:
    #     timer_label.config(text="Time's up!")

def next_question():
    global question_number, player_score,remaining_time
    
    # remaining_time=6
    
    # update_timer()

    # Simulating the next question
    question_number += 1
    question_label.config(text=f"Question {question_number}")

    # Simulating options for the question
    options = ["Option A", "Option B", "Option C", "Option D"]
    for i, option in enumerate(options):
        option_labels[i].config(text=option)

    # Simulating player score
    player_score += 10
    score_label.config(text=f"Score: {player_score}")

# Create the main Tkinter window
# root = tk.Tk()
# root.title("Quiz Application")

# Frame 1: Question Number and Timer
# frame1 = tk.Frame(root)
# frame1.pack(pady=10)

# question_label = tk.Label(frame1, text="Question 1", font=('Helvetica', 16))
# question_label.grid(row=0, column=0, padx=10)

# timer_label = tk.Label(frame1, text="Time Remaining: 60 seconds", font=('Helvetica', 16))
# timer_label.grid(row=0, column=1, padx=10)

# Frame 2: Question and Options
# frame2 = tk.Frame(root)
# frame2.pack(pady=10)

# question_label = tk.Label(frame2, text="What is the capital of France?", font=('Helvetica', 14))
# question_label.grid(row=0, column=0, columnspan=2, pady=10)

options = ["Option A", "Option B", "Option C", "Option D"]
option_labels = []

for i, option in enumerate(options):
    option_label = tk.Label(frame2, text=option, font=('Helvetica', 12))
    option_label.grid(row=i+1, column=0, pady=5)
    option_labels.append(option_label)

score_label = tk.Label(frame2, text="Score: 0", font=('Helvetica', 12))
score_label.grid(row=5, column=0, columnspan=2, pady=10)

# Button to simulate moving to the next question
next_question_button = tk.Button(frame2, text="Next Question", command=next_question)
next_question_button.grid(row=6, column=0, columnspan=2, pady=10)

# Global variables
remaining_time = 6
question_number = 1
player_score = 0

# Start the timer
# update_timer()

# Start the Tkinter event loop
root.mainloop()
