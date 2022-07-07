import pandas as pd
import numpy as np

tweets_analysed = pd.DataFrame()

weeks = ['feb_w1_2019', 'feb_w2_2019', 'feb_w3_2019', 'feb_w4_2019', 
'mar_w1_2019', 'mar_w2_2019', 'mar_w3_2019', 'mar_w4_2019', 
'apr_w1_2019', 'apr_w2_2019', 'apr_w3_2019', 'apr_w4_2019', 
'may_w1_2019', 'may_w2_2019', 'may_w3_2019', 'may_w4_2019',
'jun_w1_2019', 'jun_w2_2019', 'jun_w3_2019', 'jun_w4_2019']

for week in weeks:
    df = pd.read_csv('./3_tweets_analysed/2019/' + str(week) + '.csv', engine='python')
    df = df[['tweet_created_at', 'mun_id', 'positive', 'negative', 'oseti_score1', 'oseti_score2']]
    tweets_analysed = pd.concat([tweets_analysed, df], axis = 0, ignore_index = True)
    print(week)

tweets_analysed['tweet_created_at'] = pd.to_datetime(tweets_analysed['tweet_created_at'], errors='coerce')

tweets_analysed['date'] = tweets_analysed['tweet_created_at'].dt.date

tweets_average = pd.pivot_table(tweets_analysed, values=['positive', 'negative', 'oseti_score1', 'oseti_score2'], index=['date', 'mun_id'], aggfunc=np.mean)
tweets_average = tweets_average.reset_index()
tweets_average['mun_id'] = tweets_average['mun_id'].astype(str)
tweets_average['mun_id'] = tweets_average['mun_id'].str[:-2]
tweets_average = tweets_average.rename(columns = {'negative':'mean_negative', 'positive':'mean_positive', 'oseti_score1':'mean_oseti_score1', 'oseti_score2':'mean_oseti_score2'})

tweets_max = pd.pivot_table(tweets_analysed, values=['positive', 'negative', 'oseti_score1', 'oseti_score2'], index=['date', 'mun_id'], aggfunc=np.max)
tweets_max = tweets_max.reset_index()
tweets_max['mun_id'] = tweets_max['mun_id'].astype(str)
tweets_max['mun_id'] = tweets_max['mun_id'].str[:-2]
tweets_max = tweets_max.rename(columns = {'negative':'max_negative', 'positive':'max_positive', 'oseti_score1':'max_oseti_score1', 'oseti_score2':'max_oseti_score2'})

tweets_min = pd.pivot_table(tweets_analysed, values=['positive', 'negative', 'oseti_score1', 'oseti_score2'], index=['date', 'mun_id'], aggfunc=np.min)
tweets_min = tweets_min.reset_index()
tweets_min['mun_id'] = tweets_min['mun_id'].astype(str)
tweets_min['mun_id'] = tweets_min['mun_id'].str[:-2]
tweets_min = tweets_min.rename(columns = {'negative':'min_negative', 'positive':'min_positive', 'oseti_score1':'min_oseti_score1', 'oseti_score2':'min_oseti_score2'})

tweets_count = pd.pivot_table(tweets_analysed, values=['positive'], index=['date', 'mun_id'], aggfunc = 'count')
tweets_count = tweets_count.reset_index()
tweets_count['mun_id'] = tweets_count['mun_id'].astype(str)
tweets_count['mun_id'] = tweets_count['mun_id'].str[:-2]
tweets_count = tweets_count.rename(columns = {'positive':'tweet_count'})

tweets_variance = pd.pivot_table(tweets_analysed, values=['positive', 'negative', 'oseti_score1', 'oseti_score2'], index=['date', 'mun_id'], aggfunc=np.var)
tweets_variance = tweets_variance.reset_index()
tweets_variance['mun_id'] = tweets_variance['mun_id'].astype(str)
tweets_variance['mun_id'] = tweets_variance['mun_id'].str[:-2]
tweets_variance = tweets_variance.rename(columns = {'negative':'variance_negative', 'positive':'variance_positive', 'oseti_score1':'variance_oseti_score1', 'oseti_score2':'variance_oseti_score2'})

tweets_agg = tweets_count.merge(tweets_average, how = 'outer', on = ['date', 'mun_id'])
tweets_agg = tweets_agg.merge(tweets_min, how = 'outer', on = ['date', 'mun_id'])
tweets_agg = tweets_agg.merge(tweets_max, how = 'outer', on = ['date', 'mun_id'])
tweets_agg = tweets_agg.merge(tweets_variance, how = 'outer', on = ['date', 'mun_id'])

tweets_agg.to_csv('./4_tweets_aggregated/tweets_agg.csv', index = False)