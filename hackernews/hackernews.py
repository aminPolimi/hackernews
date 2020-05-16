from bs4 import BeautifulSoup
import requests
import validators
import json
import sys


home = 'https://news.ycombinator.com/'
data = []


def validate_uri(uri):
    """
    Check if a url is valid
    :param uri: string
        The url of a post
    :return: bool
        True means valid url and False is invalid url
    """
    try:
        if 'http://' not in uri or 'https://' not in uri:
            uri = home + uri
        valid = validators.url(uri)
        return valid
    except ValueError as err:
        print(err)
        return False


def get_news(n):
    """
    Scrap Hackernews posts and return list of post's description
    :param n: int
        Number of posts is going to be extracted
    :return: list of dictionary
        List of posts with some extra data: uri, comments, points, author, rank, title
    """
    page = 1
    i=0
    validate = True
    rank = 0
    uri = ''
    title = ''
    while i < n:  # every page has 30 posts. We have a loop on every page to reach n variable
        req = requests.get(home+'news?p=' + page.__str__())  # get content of a web page
        req.encoding = req.apparent_encoding
        page = page + 1
        html = req.text
        soup = BeautifulSoup(html, features='html.parser')  # pull data out of HTML, and parse idiomatic ways of navigating, searching, and modifying the parse tree
        rows = soup.find('table', class_='itemlist').find_all('tr')  # find the table which has posts
        for row in rows:  # loop on every table's row. past's info extracted from three rows
            if i >= n:  # We do not continue when the number of extracted posts reaches to n
                return
            hasclass = row.get('class')
            if hasclass is not None and hasclass[0] == 'athing':  # some post's info exists in a row where class=athing
                rank = int(row.find('span', class_='rank').string.replace('.', '').strip())
                a = row.find("a", class_="storylink")
                uri = a['href']
                title = a.string
                if len(title) > 256:  # check if the length of title does not exceed 256 characters
                    validate = False
                if not validate_uri(uri):  # call validate_uri function to validate url
                    validate = False
                data.append({'rank': rank, 'uri': uri, 'title': title})
            elif hasclass is None:  # some other post's info exists in a row where there is no class
                subtext = row.find("td", class_="subtext")
                if subtext is not None:
                    author = subtext.find("a", class_="hnuser").string
                    if len(author) > 256:  # check if the length of author does not exceed 256 characters
                        validate = False
                    points = int(subtext.find("span", class_="score").string.replace('points', '').strip())  # extract points
                    comm = subtext.find_all("a")[-1].string  # comment data is exists in the last a tag
                    if 'comment' in comm:  # if the latest a tag is comment
                        comments = int(comm.replace('comment', '').replace('s', '').strip())  # extract number from text
                    else:
                        comments = None
                    if validate:  # take post's info if all the data are valid
                        data[i] = {"title": title, "uri": uri, "author": author, "points": points, "comments": comments, "rank": rank}
                        i = i + 1   # goes to the next post
                    else:
                        print(rank.__str__() + ' error')


params = sys.argv
if params[1].lower() == 'hackernews' and params[2].lower() == '--posts':  # check input parameters
    try:
        n = int(params[3])
        if n > 100:   # number of posts must not exceed 100
            print('The number of posts must not more than 100')
        else:
            get_news(n)
            js = json.dumps(data)  # convert dictionary to json format
            print(js)
    except:
        print('Wrong input')
else:
    print('Wrong input parameters')