import sys

from functions import get_test, get_problem

TEXT = """
Введите номер предмета
1.Математика
2.Физика
3.Инофрматика
4.Химия
5.Русский язык
6.Биология
7.Английский язык
8.География
9.Немецкий
10.Обществознание
11.Французский
12.Литература
13.Испансикй
14.История
"""
SUBJECTS = {1: "math",
                2:"phys",
                3:"inf",
                4:"chem",
                5: "rus",
                6:"bio",
                7:"en",
                8:"geo",
                9:"de",
                10:"soc",
                11:"fr",
                12:"lit",
                13:"sp",
                14:"hist"}
if __name__ == "__main__":

    try:
        subject = SUBJECTS[int(input(TEXT))]
        SAMPLE_URL = f"https://{subject}-ege.sdamgia.ru"
    except Exception:
        print("Вы ввели неправильный номер")
        sys.exit()

    test_id = int(input('Введите test id, его вы найдете в ссылке на тест'))
    list_q = get_test(test_id, SAMPLE_URL)
    s = ''
    for q in list_q:
        s = f'{s} {str(q)}'
    print(s)
    res = []
    i=1
    for problem in list_q:
        res.append(get_problem(int(problem), SAMPLE_URL))
        print(f"done number {i}")
        i += 1
    print("Все готово, смотрите ответы в res.txt")
    with open('res.txt', 'w') as file:
        cnt = 1
        for item in res:
            file.write(f"{cnt}) {item} \n")
            cnt += 1




