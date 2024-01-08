from requests import get
from bs4 import BeautifulSoup


def extract_wwr_job(keyword):
    url = f"https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term={keyword}"
    request = get(url)
    result = []
    if request.status_code == 200:
        soup = BeautifulSoup(request.text, "html.parser")
        jobs = soup.find_all('section', class_="jobs")
        for job in jobs:
            posts = job.find_all('li')
            posts.pop(-1)
            for post in posts:
                anchors = post.find_all('a')
                anchor = anchors[1]
                links = anchor['href']
                title = anchor.find('span', class_="title")
                company = anchor.find('span', class_="company")
                location = anchor.find('span', class_="region")
                job_data = {
                    'name': f"\n{title.string.replace(',', ' ')}",
                    'company': company.string.replace(',', ' '),
                    'location': location.string.replace(',', ' '),
                    'link': f"https://weworkremotely.com/{links}"
                }
                result.append(job_data)
    else:
        print("Wrong Request!")

    return result
