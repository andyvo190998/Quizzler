THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain



class QuizInterface:

    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.score = 0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20,pady=20)
        self.score_label = Label(text=f"Score: 0", fg="white",bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)


        self.canvas = Canvas(width=300, height=230,bg="white")
        self.question_text = self.canvas.create_text(150,125,width=280,text="this is the question",fill=THEME_COLOR)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)


        correct_img = PhotoImage(file="porfolio/quizzler-app/images/true.png")
        wrong_img = PhotoImage(file="porfolio/quizzler-app/images/false.png")

        self.correct_button = Button(image=correct_img, highlightthickness=0, command=self.correct)
        self.wrong_button = Button(image=wrong_img, highlightthickness=0,command=self.wrong)

        self.correct_button.grid(column=0,row=2)
        self.wrong_button.grid(column=1,row=2)

        self.get_next_question()


        self.window.mainloop()

    def correct(self):
        is_right = self.quiz.check_answer("True")
        self.user_feedback(is_right)

    def wrong(self):
        is_right = self.quiz.check_answer("False")
        self.user_feedback(is_right)

    def user_feedback(self,is_right):
        if is_right == True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.window.after(1000, self.get_next_question)

    def get_next_question(self):
        self.canvas.config(bg="white")
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)