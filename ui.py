THEME_COLOR = "#375362"

from tkinter import *
from quiz_brain import QuizBrain
# global answer_text
class QuizInterface:

    def __init__(self, quiz_brain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.canvas = Canvas(width= 300, height=250, background='white')
        self.question_text = self.canvas.create_text(150, 125, text='Some question', fill=THEME_COLOR, font=('arial', 16, 'normal'), width=280)
        self.canvas.grid(column=0, row=1, columnspan=2 ,padx=20, pady=20)

        self.score = Label(text='Score = 0', fg='white', background=THEME_COLOR, font=('arial', 16, 'normal'),)
        self.score.config(padx=20, pady=20,)
        self.score.grid(column= 1, row= 0)

        true_img = PhotoImage(file='./images/true.png')
        self.true = Button(image=true_img, background=THEME_COLOR, padx=20, pady=20, command=self.true_press)
        self.true.grid(column=0, row=2)

        false_img = PhotoImage(file='./images/false.png')
        self.false = Button(image=false_img, background=THEME_COLOR, padx=20, pady=20, command=self.false_press)
        self.false.grid(column=1, row=2)
        self.next_question()


        self.window.mainloop()

    def next_question(self):
        
        self.canvas.config(background='white')
        self.true.config(command=self.true_press)
        self.false.config(command=self.false_press)
        self.canvas.itemconfig(self.question_text, fill=THEME_COLOR)
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)


    def true_press(self):
        self.answer_text = self.quiz.check_answer('true')
        self.canvas.itemconfig(self.question_text, text=self.answer_text)
        self.false.config(command=NONE)
        self.true.config(command=NONE)
        self.give_feedback()

    def false_press(self):
        self.answer_text = self.quiz.check_answer('false')
        self.canvas.itemconfig(self.question_text, text=self.answer_text)
        self.true.config(command=NONE)#tambien se puede colocar command= 'disabled'
        self.false.config(command=NONE)
        self.give_feedback()
        

    def give_feedback(self):
        if self.answer_text == 'You got it right!':
            self.canvas.config( background='green')
            self.canvas.itemconfig(self.question_text, fill = 'white')
        
        else:
            self.canvas.config( background='red')
            self.canvas.itemconfig(self.question_text, fill = 'white')
            
        self.window.after(2000, func=self.game_over)
        self.score.config(text=f'Score: {self.quiz.score}')
        

    def game_over(self):
        if self.quiz.still_has_questions():
            self.next_question()
        
        else: 
            self.canvas.config(background='blue')
            self.canvas.itemconfig(self.question_text, text=f'You completed the quiz\n'
                                   f'Your final Score is {self.quiz.score}')
            self.score.config(text='')
