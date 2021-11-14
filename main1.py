def task_1():
    with open('quotes.txt', 'r') as f:
        print(f.read())

    with open('quotes.txt', 'a') as f:
        aut = input('Введи автора:')
        f.write(f'\n({aut})\n')

def task_2():
    inp = ''
    citate = ''
    autor = ''
    first = True
    try:
        while inp != 'нет':
            if first:
                inp = input("Не хотите добать автора?").lower()
                first = False
            else:
                citate = input("""Ну давай вводи свою цитатУ!!!!
                """)
                autor = input("""Ну а автор????????
                """)
                with open('quotes.txt', 'a') as Fiel:
                    Fiel.write(f'\n{citate}\n({autor})\n')
                inp = input('Добавишь ещё????????????????????????? ').lower()
        with open('quotes.txt', 'r') as File:
            data_sps = File.read().split('\n')
            for e in data_sps:
                if e != '':
                    if e[0] == '(':
                        print(f"""
        --- {e}
        """)
    except IOError:
        print("""
        Фаил не найден!
        """)

def ProdTask1():
    class Pupil():
        def __init__(self, surname, name, grade):
            self.surname = surname
            self.name = name
            self.grade = grade
    pupils = []
    bests = []
    middle_grade = 0
    with open('pupils.txt', 'r') as file:
        data = file.readlines()
        for i in data:
            l = i.split(' ')
            pupils.append(Pupil(l[0], l[1], i[-2]))
    for e in pupils:
        middle_grade += int(e.grade)
        if e.grade == '5':
            bests.append(e.surname)
    middle_grade = middle_grade/len(pupils)
    print(f"""
    Среняя оценка: {middle_grade}
    Отличники: {bests}
""")



if __name__ == '__main__':
    ProdTask1()