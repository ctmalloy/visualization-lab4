import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')
#df['Date'] = pd.to_datetime(df['Date'])

# Preparing data
# trace 1
new_df = df.groupby(['month'])['actual_max_temp'].transform('max') == df['actual_max_temp']
new_df = df.loc[new_df]
# Sorting values
new_df = new_df.sort_values(by=['month'])
trace1 = go.Scatter(x=new_df['month'], y=new_df['actual_max_temp'], mode='lines', name='Actual Max Temp')
# trace 2
new_df = df.groupby(['month'])['actual_min_temp'].transform('min') == df['actual_min_temp']
new_df = df.loc[new_df]
# Sorting values
new_df = new_df.sort_values(by=['month'])
trace2 = go.Scatter(x=new_df['month'], y=new_df['actual_min_temp'], mode='lines', name='Actual Min Temp')
# trace 3
# Sorting values
new_df = df.sort_values(by=['month']).groupby(['month']).actual_mean_temp.mean()
trace3 = go.Scatter(x=new_df.index, y=new_df, mode='lines', name='Actual Mean Temp')

data = [trace1, trace2, trace3]

# Preparing layout
layout = go.Layout(title='Actual Max, Min and Average Temperatures', xaxis_title='Month', yaxis_title='Temperature')

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='multilinechart.html')