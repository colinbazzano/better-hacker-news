import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com')
res_page_2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res_page_2.text, 'html.parser')
# grabs all elements with the class 'score'
# print(soup.select('.score'))
# this will find all of the divs, or whatever you specify
# print(soup.find_all('div'))
# print(soup.find('a'))
links = soup.select('.storylink')
links2 = soup2.select('.storylink')
subtext = soup.select('.subtext')
subtext2 = soup2.select('.subtext')

combined_links = links + links2
combined_subtext = subtext + subtext2


def sort_stories_by_votes(hnlist):
    # for sorting by votes
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    # new hacker news list
    hn = []
    for index, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        # turn the votes into integers and remove the points at the end
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            # print(points)
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(combined_links, combined_subtext))
