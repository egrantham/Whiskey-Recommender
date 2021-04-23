# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 15:50:22 2021

@author: Ethan
"""

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as soup

def getSoup(link):
    """ Given a link, instantiate the page_soup parser and return it """
    # open connection w/ main page, read html
    hdr = {'User-Agent': 'Mozilla/5.0'}
    try:
        req = Request(link,headers=hdr)
        uClient = urlopen(req)
        page_html = uClient.read()
        uClient.close()
            # instantiate html parser w/ html string, return
        page_soup = soup(page_html, features="html.parser")
        return page_soup
    except: 
        pass

def readLinks(Links,names):
    soupList = {}
    count = 0
    for i in range(len(Links)):
        try:
            soup = getSoup(Links[i])
            name = names[i]
            print(count)
            count += 1
            if "old.reddit" in Links[i]:
                soupList[name] += "Old Format"
                continue
            if name in soupList:
                review = soup.select_one("div[data-testid='comment-top-meta'] + div[data-test-id='comment']")
                review_text = "".join([string for string in review.stripped_strings])
                
                if "/*# sourceMappingURL" in review_text:
                    soupList[name] += "Ignore..."
                    continue
                else:
                    soupList[name]+= review_text
                
            else:
                review = soup.select_one("div[data-testid='comment-top-meta'] + div[data-test-id='comment']")
                review_text = "".join([string for string in review.stripped_strings])
                
                if "/*# sourceMappingURL" in review_text:
                    soupList[name] = "Ignore..."
                    continue
                else:
                    soupList[name]= review_text

            [s.extract() for s in soup(['script','style'])]
        except:
            pass
    return soupList
    
def main():
    # some sample links and names to try
    links = ['https://www.reddit.com/r/bourbon/comments/5fx9u3/review_2_ransom_spirits_whippersnapper_oregon/',
    'https://old.reddit.com/r/worldwhisky/comments/b9b52y/bookers_little_book_chapter_2_noe_simple_task/?',
    'http://www.reddit.com/r/worldwhisky/comments/12efn1/wigle_white_wheat_whiskey_a_review/']
    names = ['whippersnapper','bookers','wigle wheat']
    soups = readLinks(links,names)
    print(soups)

if __name__=="__main__":
    main()