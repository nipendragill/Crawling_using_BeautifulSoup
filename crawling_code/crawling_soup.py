import urllib.request
from bs4 import BeautifulSoup

class Crawling:

    initial_page_url = 'https://www.python.org'
    list_url = []
    is_initial_page_url = True
    all_urls = []
    start_index = 0

    def parse(page_url=None):
        if page_url is not None:
            try:
                data_page = urllib.request.urlopen(page_url)
                soup = BeautifulSoup(data_page)
                all_links = soup.find_all("a")
                new_links = []
                for link in all_links:
                    new_links.append(link.get("href"))
                return new_links
            except:
                return None
        else:
            return None

    if is_initial_page_url:
        all_urls = parse(page_url=initial_page_url)
        is_initial_page_url=False

    for link in all_urls:
        if link is not None and link.startswith('http') and "#" not in link:
            list_url.append(link)

    for link in list_url:
        try:
            links = parse(page_url=list_url[start_index])
            start_index+=  1
        except:
            break

    print(list_url)


