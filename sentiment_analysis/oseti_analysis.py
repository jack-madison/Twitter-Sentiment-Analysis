from cmath import nan
import oseti
import pandas as pd
import numpy as np

analyzer = oseti.Analyzer()

tweets = pd.read_csv('https://media.githubusercontent.com/media/jack-madison/Twitter-Sentiment-Analysis/main/all_tweets/prepared_tweets/2019/feb_w1_2019.csv')

tweets['positive'] = np.nan
tweets['negative'] = np.nan

for x in range(len(tweets)):
    polarities = analyzer.count_polarity(str(tweets['tweet_text'][x]))

    positive = 0
    negative = 0

    for sentence in polarities:
        positive = positive + sentence['positive']
        negative = negative + sentence['negative']

    tweets['positive'][x] = positive
    tweets['negative'][x] = negative

    print(x)

tweets['oseti_score1'] = tweets['positive'] - tweets['negative']

tweets['oseti_score2'] = tweets['oseti_score1'] / (tweets['positive'] + tweets['negative'])

tweets['oseti_score2'] = tweets['oseti_score2'].fillna(0)

tweets.to_csv('./feb_w1_2019_oseti.csv', index = False)