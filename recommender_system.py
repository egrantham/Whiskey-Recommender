import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import sys

ds = pd.read_csv("output.csv",encoding='latin1')
#print(ds)

tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=0, stop_words='english')
tfidf_matrix = tf.fit_transform(ds['description'].apply(lambda x: np.str_(x)))

print('Input file read...')

cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)

print('Calculated similarities...')

results = {}

for idx, row in ds.iterrows():
    similar_indices = cosine_similarities[idx].argsort()[:-100:-1]
    similar_items = [(cosine_similarities[idx][i], ds['id'][i]) for i in similar_indices]

    results[str(row['id'])] = similar_items[1:]
print("Reordered similarities for Recs...")

def item(id):
    return str(ds.at[id,'description']).split('- ')[0]

# Just reads the results out of the dictionary.
def recommend(item_id, num):
    print("Recommending " + str(num) + " products similar to " + item(int(item_id)) + "...")
    print("-------")
    recs = results[item_id][:num]
    for rec in recs:
        print("Recommended: " + item(int(rec[1])) + " (score: " + str(rec[0]) + ")")
    print()

def main():        
    isFinished = False
    while not isFinished:
        isMatched = False
        my_num = int(input("How many recommendations would you like?\n"))
        item_name = input("What whiskey would you like recommendations based on?\n")
        while not isMatched:
            for idx, row in ds.iterrows():
                if str(row['description']).split('- ')[0].lower() == item_name.lower():
                    print("\nFound match at index "+str(row['id'])+": "+str(row['description']).split('- ')[0])
                    my_item_id = str(idx)
                    recommend(item_id=my_item_id, num=my_num)
                    isMatched = True
                    if input("Continue? (Enter Y/N) ").lower() == "n":
                        sys.exit(0)
            if not isMatched: 
                item_name = input("Sorry, we can't find a match. Please try another name.\n")
            
if __name__ == "__main__":
    main()

