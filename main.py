# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 16:38:12 2021

@author: Ethan
"""

class Review():
    """Represents a single whisk(e)y review"""
    def __init__(self, name, link, rating, style, price):
        self.name = name
        self.link = link
        self.rating = rating
        self.style = style
        self.price = price
    
    def toString(self):
        print(f'Whisky Name: {self.name}\n'+
              f'Link To Reddit Review: {self.link}\n'+
              f'Reviewer Rating: {self.rating}\n'+
              f'Whisky Region or Style: {self.style}\n'+
              f'Price Paid: {self.price}\n')

def convert(line):
    """Converts a line of text into the args for Review class"""
    
    line = line.split(',')
    while '\n' in line:
        line.remove('\n')
    return line

def combine(reviewList, minReviews):
    # key = name, value[0] = total rating points, value[1] = # of reviews
    whiskeyDict = {}
    count = 0
    for review in reviewList:
        count += 1
        if review.name in whiskeyDict.keys():
            #print(count, review.name)
            try:
                whiskeyDict[review.name][0] += float(review.rating)
                whiskeyDict[review.name][1] += 1
            except ValueError:
                pass
        else:
            try:
                whiskeyDict[review.name] = [float(review.rating),1]
            except ValueError:
                pass
            
    # here, we calculate the avg ratings using whiskeyDict         
    avg_ratings_Dict = {key: value[0]/value[1] for key, value in whiskeyDict.items()}
    
    # code to sort the dictionary by value
    sorted_ratings = {}
    sorted_keys = sorted(avg_ratings_Dict, key=avg_ratings_Dict.get)

    for key in sorted_keys:
        # here, restricting the list only whiskies w/ at least 50 ratings
        if whiskeyDict[key][1] >= minReviews:
            sorted_ratings[key] = avg_ratings_Dict[key]    
    return sorted_ratings

def main():
    minReviews = int(input("Minimum # of reviews? "))
    
    # TODO: add code to filter by style, price
    desiredStyle = input("Any region or style you are interested in? ")
    maxPrice = input("What is the maximum price you'd pay for a bottle? ")
    
    file = open("reddit_whisky_data.csv", "r", errors = 'ignore')
    
    categories = file.readline().split(',')
    
    reviewList = []
    count = 0
    
    for line in file:
        count += 1
        argList = convert(line)
        if len(argList) == 4:
            argList.append('N/A')
        review = Review(argList[0], argList[1], argList[2], argList[3], argList[4])
        reviewList.append(review)
    file.close()
    
    sorted_ratings = combine(reviewList, minReviews)
    
    print(str(len(sorted_ratings))+" Unique Whiskies Found:\n")
    print(sorted_ratings)
    
    #print(categories)
#    for review in reviewList:
#        review.toString()

if __name__ == "__main__":
    main()