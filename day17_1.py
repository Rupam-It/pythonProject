#this is a project where we will create a quiz model


# this is question bank which need branch of data 
question_data = [
{"text": "A slug's blood is green.", "answer": "True"},
{"text": "The loudest animal is the African Elephant.", "answer": "False"},
{"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
{"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
{"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
{"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
{"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
{"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
{"text": "Google was originally called 'Backrub'.", "answer": "True"},
{"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
{"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
{"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]




#this is question class
class Question:
    def __init__(self,text,answer):
        self.text=text
        self.answer=answer



# this is quiz class
class Quizbrain:
    def __init__(self,q_list):
        self.question_number=0
        self.question_list=q_list
        self.score=0


    def still_has_question(self):
        if self.question_number <  len(self.question_list):
            return True
        return False

    def next_question(self):
        self.question_number+=1
        print(f"Q.{self.question_number} {self.question_list[self.question_number-1].text } (true/false): ", end="")
        ans=input()
        self.cheaK_answer(ans,self.question_list[self.question_number-1].answer)


    def cheaK_answer(self,user_answer,right_answer):
        if user_answer.lower()==right_answer.lower():
            print("You got it right..")
            self.score+=1
        else: 
            print("opps wrong answer.")
        print(f"The correct answer was: {right_answer}")
        print(f"your current score is: {self.score}/{self.question_number}")
        print('\n')





# now we have to make a quesion  bank
question_bank=[]

for question in question_data:
    question_text=question['text']
    question_answer=question['answer']
    new_question=Question( question_text,question_answer)
    question_bank.append(new_question)

show=Quizbrain(question_bank)

while show.still_has_question():
    show.next_question()



print("You have completed the quiz ")
print(f"your final score was: {show.score}/{show.question_number}")