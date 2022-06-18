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
    tweets_analysed = tweets_analysed.append(df)
    print(week)

tweets_average = pd.pivot_table(tweets_analysed, values=[''], index=[''], aggfunc=np.mean)


