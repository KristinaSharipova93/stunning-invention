cheat_sheet = ''
def was_asked(memory, q):
    for question, answer in memory:
        if question == q:
            cheat_sheet = answer
            return 1
    return 0

def old_answer():
    global cheat_sheet
    rez,cheat_sheet = cheat_sheet,''
    return rez

if __name__ == 'main':
    memory = [
        ('ты меня слышишь?', 'да'),
        ('ты меня слышишь?', 'нет'),
    ]
    q = 'Ты меня слышишь?'
    print(q,was_asked(memory, q))
    print (q,old_answer ( memory, q) )
    print ( q,old_answer (memory, q) )