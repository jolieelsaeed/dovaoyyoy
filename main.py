import requests
from bs4 import BeautifulSoup

page = 0
job_title = []
while True:
    result = requests.get(f"https://reliefweb.int/jobs?page={page}")
    src = result.content
    soup = BeautifulSoup(src,"html.parser")
    # print(soup)
    job_titles = soup.find_all("h3", {"class": "rw-river-article__title"})
    for i in range(len(job_titles)):
        job_title.append(job_titles[i].text.strip().replace("\n",""))
    print(f"page {page} is switched")
    page += 1
    if page > 5:
        break
print(job_title)