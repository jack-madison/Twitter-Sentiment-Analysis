import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
from plotnine import *
from binsreg import *

df = pd.read_stata('./4_tweets_aggregated/twitter_mun_cleaned2.dta')

est = binsreg(x = 'ln_pollen_t999', y = 'mean_oseti_score1', data = df)