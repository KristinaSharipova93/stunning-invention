"""
    да нет
"""
from random import randint
from module import was_asked,old_answer

memory = []
promprt = "Задайте вопрос"
answers = ("да", "нет", "незнаю")
question = " "
while question != "хватит":
    print(promprt, end = '')
    question = input("")
    if was_asked(memory, question):
        print(old_answer())
    else:
        answer = answers[randint(0,len(answers)-1)]
        print(answer)
        memory += [(question,answer)]
