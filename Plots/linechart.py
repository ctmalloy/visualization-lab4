import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')
#df['date'] = pd.to_datetime(df['date'])

new_df = df.groupby(['month'])['actual_max_temp'].transform('max') == df['actual_max_temp']
new_df = df.loc[new_df]

# Preparing data
data = [go.Scatter(x=new_df['month'], y=new_df['actual_max_temp'], mode='lines', name='Max Temp')]

# Preparing layout
layout = go.Layout(title='Actual Max Temperature by Month', xaxis_title='Month', yaxis_title='Max Temp')

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='linechart.html')