import tkinter as tk

class QuestionSet:

    def __init__(self, questionSet):

        self.question = questionSet
        self.answer_options = []
        for counter in range(len(questionSet)-1):
            answer_option = tk.Radiobutton(text=questionSet[counter])
            answer_option.grid(row=2, column=counter)
            self.answer_options.append(answer_option)

def button_press(btn):
    global question
    question = btn.question
    questionStatement.set(question)

# List of questions and their possible answers
question1 = QuestionSet(["What do you think?", "Yes", "No"])
question2 = QuestionSet(["Assessment 2", "Yes", "No", "Maybe"])
question3 = QuestionSet(["Assessment 3", "Agree", "Disagree"])
question4 = QuestionSet(["Assessment 4", "Yes", "No"])

# Display Questions
questionStatement = tk.StringVar()
questionStatement.set(question1.question)
questionField = tk.Label(textvariable=questionStatement)
questionField.grid(columnspan=100, sticky="E")

# button to select questions to be answered
button1 = tk.Button(text="Strongly Agree", command=lambda: button_press(question1))
button2 = tk.Button(text="Agree ", command=lambda: button_press(question2))
button3 = tk.Button(text="Neutral", command=lambda: button_press(question3))
button4 = tk.Button(text="Disagre", command=lambda: button_press(question4))

button1.grid(row=4, column=4)
button2.grid(row=4, column=5)
button3.grid(row=4, column=6)
button4.grid(row=4, column=7)

root = tk.Tk()
root.mainloop()
