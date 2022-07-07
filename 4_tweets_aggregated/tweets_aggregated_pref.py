import pandas as pd
import numpy as np

tweets_analysed = pd.DataFrame()

weeks = ['feb_w1_2018', 'feb_w2_2018', 'feb_w3_2018', 'feb_w4_2018', 
'mar_w1_2018', 'mar_w2_2018', 'mar_w3_2018', 'mar_w4_2018', 
'apr_w1_2018', 'apr_w2_2018', 'apr_w3_2018', 'apr_w4_2018', 
'may_w1_2018', 'may_w2_2018', 'may_w3_2018', 'may_w4_2018',
'jun_w1_2018', 'jun_w2_2018', 'jun_w3_2018', 'jun_w4_2018']

for week in weeks:
    df = pd.read_csv('./' + str(week) + '_oseti.csv', engine='python')
    df = df[['tweet_created_at', 'prefid', 'positive', 'negative', 'oseti_score1', 'oseti_score2']]
    tweets_analysed = pd.concat([tweets_analysed, df], axis = 0, ignore_index = True)
    print(week)

tweets_analysed['tweet_created_at'] = pd.to_datetime(tweets_analysed['tweet_created_at'], errors='coerce')

tweets_analysed['date'] = tweets_analysed['tweet_created_at'].dt.date

tweets_average = pd.pivot_table(tweets_analysed, values=['positive', 'negative', 'oseti_score1', 'oseti_score2'], index=['date', 'prefid'], aggfunc=np.mean)
tweets_average = tweets_average.reset_index()
tweets_average['prefid'] = tweets_average['prefid'].astype(str)
tweets_average['prefid'] = tweets_average['prefid'].str[:-2]
tweets_average = tweets_average.rename(columns = {'negative':'mean_negative', 'positive':'mean_positive', 'oseti_score1':'mean_oseti_score1', 'oseti_score2':'mean_oseti_score2'})

tweets_max = pd.pivot_table(tweets_analysed, values=['positive', 'negative', 'oseti_score1', 'oseti_score2'], index=['date', 'prefid'], aggfunc=np.max)
tweets_max = tweets_max.reset_index()
tweets_max['prefid'] = tweets_max['prefid'].astype(str)
tweets_max['prefid'] = tweets_max['prefid'].str[:-2]
tweets_max = tweets_max.rename(columns = {'negative':'max_negative', 'positive':'max_positive', 'oseti_score1':'max_oseti_score1', 'oseti_score2':'max_oseti_score2'})

tweets_min = pd.pivot_table(tweets_analysed, values=['positive', 'negative', 'oseti_score1', 'oseti_score2'], index=['date', 'prefid'], aggfunc=np.min)
tweets_min = tweets_min.reset_index()
tweets_min['prefid'] = tweets_min['prefid'].astype(str)
tweets_min['prefid'] = tweets_min['prefid'].str[:-2]
tweets_min = tweets_min.rename(columns = {'negative':'min_negative', 'positive':'min_positive', 'oseti_score1':'min_oseti_score1', 'oseti_score2':'min_oseti_score2'})

tweets_count = pd.pivot_table(tweets_analysed, values=['positive'], index=['date', 'prefid'], aggfunc = 'count')
tweets_count = tweets_count.reset_index()
tweets_count['prefid'] = tweets_count['prefid'].astype(str)
tweets_count['prefid'] = tweets_count['prefid'].str[:-2]
tweets_count = tweets_count.rename(columns = {'positive':'tweet_count'})

tweets_variance = pd.pivot_table(tweets_analysed, values=['positive', 'negative', 'oseti_score1', 'oseti_score2'], index=['date', 'prefid'], aggfunc=np.var)
tweets_variance = tweets_variance.reset_index()
tweets_variance['prefid'] = tweets_variance['prefid'].astype(str)
tweets_variance['prefid'] = tweets_variance['prefid'].str[:-2]
tweets_variance = tweets_variance.rename(columns = {'negative':'variance_negative', 'positive':'variance_positive', 'oseti_score1':'variance_oseti_score1', 'oseti_score2':'variance_oseti_score2'})

tweets_agg = tweets_count.merge(tweets_average, how = 'outer', on = ['date', 'prefid'])
tweets_agg = tweets_agg.merge(tweets_min, how = 'outer', on = ['date', 'prefid'])
tweets_agg = tweets_agg.merge(tweets_max, how = 'outer', on = ['date', 'prefid'])
tweets_agg = tweets_agg.merge(tweets_variance, how = 'outer', on = ['date', 'prefid'])

tweets_agg.to_csv('./oseti_tweets_pref_2018.csv', index = False)