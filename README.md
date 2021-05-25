# Whiskey-Recommender

A project to recommend whiskies using public reviews and data. I gathered data compiled from [The Reddit Whisky Network Review Archive
 ](https://docs.google.com/spreadsheets/d/1X1HTxkI6SqsdpNSkSSivMzpxNT-oeTbjFFDdEkXD30o/edit#gid=695409533). My goal for this project was to allow users to specify some desired traits of a whiskey or name a whiskey they like and have the program recommend a few for them. This was a project for my Computer Science seminar class.

# What I Learned

* I improved my scraping skills with BeautifulSoup 
* Conceptual knowledge on TF-IDF as a text-classification feature and cosine similarity
* The basics of using scikit-learn

# To Run The Program

1. Clone this repository
2. Make sure you have installed a recent version of Python [here](https://www.python.org/downloads/). As of writing this I believe 3.7 or later should be fine. 
3. There are two versions of this program. Version 1.0 in main.py and Version 2.0 in recommender_system.py. Version 1.0 allows you to specify some traits of the whiskey, while Version 2.0 uses a similarity metric to reommend similar whiskies to ones you like.
4. Run either the main.py file or the recommender_system.py from the command line or your favorite IDE.
5. Version 1.0 will ask for user input on the desired # of reviews, the region/style, and the price range. Version 2.0 will ask for a whiskey to base recommendations off and the desired # of recommendations. Enter this information and enjoy the results! 
