import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px

df=pd.read_csv('Time series.csv')

print(df.columns)

bar1=px.bar(df,x='Date',y='West',color='West',
       height=500,hover_data=['Date','West'])
print(bar1)