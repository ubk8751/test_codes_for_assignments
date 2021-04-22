import pandas as pd

dafr = {"u_names": ["@tweeter1"], "tweets": ["This is an example Tweet for the interesting #DataAnalysis course at #BTH-2021. The #AI_students taking the course are quite lucky ;)."]}

def hash_getter (data_frame):
    # Turn the dataframe back into a dictionary
    df = data_frame.to_dict ()
    hashtags = []
    ends = [".", ",", "!", "?", ":", ";"]
    # Circle trough the tweets
    for tweet_number in df["tweets"]:
        tweet = df["tweets"][tweet_number]
        lst_tweet = tweet.split(" ")
    
        # Circle through every word in each tweet
        for word in lst_tweet :
            letters = list(word)
            # Add the hashtag to the list
            if letters [0] == "#":
                if letters [-1] not in ends:
                    hashtags.append(word)
                else:
                    word = word [:-1]
                    hashtags.append(word)
    
    # Return the list of hashtags to do something with
    return hashtags

if __name__ == "__main__":
    data_frame = pd.DataFrame(dafr)
    hashes = hash_getter(data_frame)
    print(hashes)

