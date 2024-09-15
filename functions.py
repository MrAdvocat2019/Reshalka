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