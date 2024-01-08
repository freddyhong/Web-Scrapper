from requests import get
from bs4 import BeautifulSoup


def extract_rok_job(keyword):
    url = f"https://remoteok.com/remote-{keyword}-jobs"
    request = get(url, headers={"User-Agent": "Kimchi"})
    job_data = []
    result = []
    if request.status_code == 200:
        soup = BeautifulSoup(request.text, "html.parser")
        posts = soup.find_all('td', class_="company_and_position")
        for post in posts:
            anchors = post.find_all('a')
            anchor = anchors[0]
            links = anchor['href']
            job = post.find('h2')
            company = post.find('h3')
            location = post.find('div', class_="location")
            if location is not None:
                flag = location.string.replace(",", " ")
            else:
                flag = location
            # salery = post.find('div', class_="location tooltip")
            job_data = {
                'name': job.string[:-1].replace(",", " "),
                'company': company.string[1:-1].replace(",", " "),
                'location': flag,
                # 'salery': salery.string,
                'link': f"https://remoteok.com/{links}"
            }
            result.append(job_data)
    else:
        print("Wrong Request")
    result.pop(0)
    return result
