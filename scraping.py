import requests
from bs4 import BeautifulSoup

url = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

result = soup.find(id='ResultsContainer')

job_elems = result.find_all('section', class_='card-content')

# Separando os resultado dos elementos

# Listando todos os resultados da pagina
for job_elem in job_elems:
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    if None in (title_elem, company_elem, location_elem):
        continue
    print(f'{title_elem.text.strip()} \n {company_elem.text.strip()} \n {location_elem.text.strip()}  \n *****')


# Filtrando o resultado
python_jobs = result.find_all('h2', 
                            string=lambda text:'python' in text.lower())

print('\nFiltrando Resultado (PYTHON): \n')
for py_job in python_jobs:
    link = py_job.find('a')['href']
    print(py_job.text.strip())
    print(f'Acesse Aqui: {link}\n ')