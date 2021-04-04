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
        return (f'Whisky Name: {self.name}\n'+
              f'Link To Reddit Review: {self.link}\n'+
              f'Reviewer Rating: {self.rating}\n'+
              f'Whisky Region or Style: {self.style}\n'+
              f'Price Paid: {self.price}\n')
        
class Whiskey():
    """Represents a single whisk(e)y"""
    def __init__(self, name, rating, style, price):
        self.name = name
        self.rating = rating
        self.style = style
        self.price = price
    
    def toString(self):
        s = (f'Whisky Name:            {self.name}\n'+
             f'Avg. Reviewer Rating:  {self.rating : 2.2f}\n'+
             f'Region or Style:        {self.style}\n')
        # this block handles the price info whether it is available or not
        if self.price != -1.0:
            s += (f'Avg. Price Paid:        ${self.price : 4.2f}\n')
        else:
            s += (f'Avg. Price Paid:        Unavailable\n')
        return s

def convert(line):
    """Converts a line of text into the args for Review class"""
    
    line = line.split(',')
    while '\n' in line:
        line.remove('\n')
    return line

def combine(reviewList, minReviews, desiredStyle, maxPrice):
    
    # loop to aggregate the reviews 
    whiskeyDict = {}
    for review in reviewList:
        if review.name in whiskeyDict.keys():
            try:
                whiskeyDict[review.name]['reviewTotal'] += float(review.rating)
                whiskeyDict[review.name]['num'] += 1
            except ValueError:
                pass
        else:
            try:
                whiskeyDict[review.name] = {'reviewTotal':float(review.rating),
                                             'num':1, 'style': review.style}
            except ValueError:
                pass
    
    # loop to aggregate the prices        
    priceDict = {}
    for review in reviewList:
        if review.name in priceDict.keys():
            if review.price != -1.0:
                priceDict[review.name]['priceTotal'] += review.price
                priceDict[review.name]['num'] += 1
        else:
            if review.price != -1.0:
                priceDict[review.name] = {'priceTotal': review.price,
                                             'num':1}
            
    # here, we calculate the avg ratings and prices using whiskeyDict and priceDict         
    avg_ratings_Dict = {key: value['reviewTotal']/value['num'] for key, value in whiskeyDict.items()}
    avg_price_Dict = {key: value['priceTotal']/value['num'] for key, value in priceDict.items()}
    
    # code to sort by rating
    sorted_ratings = []
    sorted_keys = sorted(avg_ratings_Dict, key=avg_ratings_Dict.get)

    for key in sorted_keys:
        # here, restricting the list only whiskies that match the desired style, price and # of reviews
        if key in avg_price_Dict.keys():
            if whiskeyDict[key]['num'] >= minReviews and avg_price_Dict[key] <= maxPrice and whiskeyDict[key]['style'].lower() == desiredStyle.lower() :  
                sorted_ratings.append(Whiskey(key,avg_ratings_Dict[key],whiskeyDict[key]['style'], avg_price_Dict[key]))
        else:
            if whiskeyDict[key]['num'] >= minReviews and whiskeyDict[key]['style'].lower() == desiredStyle.lower() :  
                sorted_ratings.append(Whiskey(key,avg_ratings_Dict[key],whiskeyDict[key]['style'], -1.0))
    return sorted_ratings

def makeFloat(s):
 # this function will force the price to be a float or -1.0 if invalid 
    try:
        price = float(s)
    except ValueError:
        price = -1.0
    return price

def readFile():    
    file = open("reddit_whisky_data.csv", "r", errors = 'ignore')
    # we're not doing anything with categories yet... but we might
    categories = file.readline().split(',')
    
    reviewList = []
    count = 0
    
    # for every line, create a Review object and add it to the list
    for line in file:
        count += 1
        argList = convert(line)
        if len(argList) == 4:
            argList.append('N/A')
        argList[4] = makeFloat(argList[4])
        review = Review(argList[0], argList[1], argList[2], argList[3], argList[4])
        reviewList.append(review)
    file.close()
    return reviewList

def main():
    # getting input
    minReviews = int(input("Minimum # of reviews? "))
    desiredStyle = input("Any region or style you are interested in? ")
    maxPrice = float(input("What is the maximum price you'd pay for a bottle? "))

    # read file, combine data into list
    reviewList = readFile()
    sorted_ratings = combine(reviewList, minReviews, desiredStyle, maxPrice)
    
    # output
    print("\n"+str(len(sorted_ratings))+" Unique Whiskies Found:\n")
    for whiskey in sorted_ratings:
        print(whiskey.toString())


if __name__ == "__main__":
    main()