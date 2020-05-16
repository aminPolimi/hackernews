# Hacker News
A hacker news reader written in python to get data from https://news.ycombinator.com/ and return json format.


## Features

View "top", "newest", and "show" posts from Hacker News.

Read posts using "beautifulsoup4", "validators" and "requests" in python.

[Beautiful Soup](https://pypi.org/project/beautifulsoup4/) is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree. 

[Validator](https://pypi.org/project/validators/) makes validation easy with functions like url() to check if input parameter is a valid URL or not.

[Requests](https://pypi.org/project/requests/) is a Python HTTP library. The goal of the project is to make HTTP requests simpler and more human-friendly.


## Output format:

[

    {
    
        "title": "Web Scraping in 2016",
        
        "uri": "https://franciskim.co/2016/08/24/dont-need-no-stinking-api-web-scraping-2016-beyond/",
        
        "author": "franciskim",
        
        "points": 133,
        
        "comments": 80,
        
        "rank": 1
        
    },
    
    {
    
        "title": "Instapaper is joining Pinterest",
        
        "uri": "http://blog.instapaper.com/post/149374303661",
        
        "author": "ropiku",
        
        "points": 182,
        
        "comments": 99,
        
        "rank": 2
        
    } 
    
]


## How to run?

1. download hackernews folder and install python requirements
```
pip install -r requirements.txt

python hackernews.py hackernews --posts 50
```
  note: 50 is the number of posts you are going to read

2. run using Docker

* clone hackernews repository

* open terminal on Mac OS or cmd on windows and go to hackernews folder
```
docker build -t "hackernews" .

docker run --name python-app hackernews
```
  note: open Dockerfile and change 50 in last line if you are going to get arbitary number of posts






