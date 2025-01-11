class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

new_ques = Question("abcd", "123")
print(new_ques.text)
print(new_ques.answer)

