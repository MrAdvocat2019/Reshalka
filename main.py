import requests
from bs4 import BeautifulSoup
SAMPLE_URL ="https://rus-ege.sdamgia.ru/problem?id="


def get_problem(problem_id):
    response = requests.get(f'https://rus-ege.sdamgia.ru/problem?id={problem_id}')
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

def get_test(testid):
        page = requests.get(
            f'https://rus-ege.sdamgia.ru/test?id={testid}')
        soup = BeautifulSoup(page.content, 'html.parser')
        return [i.text.split()[-1] for i in soup.find_all('span', {'class': 'prob_nums'})]
if __name__ == "__main__":
    test_id = int(input('test_id'))
    list_q = get_test(test_id)
    s = ''
    for q in list_q:
        s = f'{s} {str(q)}'
    print(s)
    res = []
    i=1
    for problem in list_q:
        res.append(get_problem(int(problem)))
        print(f"done number {i}")
        i += 1
    with open('res.txt', 'w') as file:
        for item in res:
        # Write the element to the file followed by a newline character
            file.write(str(item) + '\n')




    