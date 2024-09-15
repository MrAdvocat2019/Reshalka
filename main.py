import sys



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
import requests
from bs4 import BeautifulSoup
def get_problem(problem_id, sample_url):
    """returns answer to a problem with id = problem_id"""
    response = requests.get(f'{sample_url}/problem?id={problem_id}')
    if response.status_code != 200:
        print('fatal error')
    soup = BeautifulSoup(response.content, 'html.parser')
    ANSWER = ''
    prob = soup.find('div', {'class': 'prob_maindiv'})
    try:
        ANSWER = prob.find(
            'div', {'class': 'answer'}).text.replace('Ответ: ', '')
    except IndexError:
        pass
    except AttributeError:
        pass
    return ANSWER.split("|")[0]

def get_test(testid, sample_url):
    """returns all problem numbers from test with id = testid"""
    page = requests.get(
        f'{sample_url}/test?id={testid}')
    soup = BeautifulSoup(page.content, 'html.parser')
    return [i.text.split()[-1] for i in soup.find_all('span', {'class': 'prob_nums'})]

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





