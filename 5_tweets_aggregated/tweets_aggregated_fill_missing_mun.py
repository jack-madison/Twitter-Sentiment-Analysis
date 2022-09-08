import pandas as pd
from datetime import date, timedelta

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

mun_list = pd.read_csv('./5_tweets_aggregated/mun_list.csv')

start_date = date(2014, 2, 1)
end_date = date(2014, 7, 1)

df = pd.DataFrame()

for single_date in daterange(start_date, end_date):
    mun_list['date'] = single_date.strftime("%Y-%m-%d")
    df = pd.concat([df, mun_list])

df = df[['date', 'mun_id', 'municipality', 'prefid', 'pref', 'mun_X', 'mun_Y']]

tweets_agg = pd.read_csv('./5_tweets_aggregated/2014/tweets_agg_mun_2014.csv')

df = pd.merge(df, tweets_agg, how = 'left', on = ['date', 'mun_id'])

df['tweet_count'] = df['tweet_count'].fillna(0)

df.to_csv('./5_tweets_aggregated/2014/oseti_tweets_mun_2014.csv', index = False)