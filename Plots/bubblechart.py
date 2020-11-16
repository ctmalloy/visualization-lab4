import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../Datasets/Weather2014-15.csv')
# Removing empty spaces from State column to avoid errors
#df = df.apply(lambda x: x.str.strip() if x.dtype == 'object' else x)

# Creating unrecovered column
#df['Unrecovered'] = df['Confirmed'] - df['Deaths'] - df['Recovered']

# Removing China and Others from data frame
#df = df[(df['Country'] != 'China') & (df['Country'] != 'Others')]

# Creating average actual temperature for each type month Column
#new_df = df.groupby(['month']).agg(
#{'Confirmed': 'sum', 'Recovered': 'sum', 'Unrecovered': 'sum'}).reset_index()

#Average Actual Max Temp
max_df = df.sort_values(by=['month']).groupby(['month']).actual_max_temp.mean()

#Average Actual Min Temp
min_df = df.sort_values(by=['month']).groupby(['month']).actual_min_temp.mean()

# Preparing data
data = [
    go.Scatter(x=min_df,
                y=max_df,
                text=max_df.index,
                mode='markers',
                marker=dict(size=max_df,
                            color=max_df, showscale=True))
]

# Preparing layout
layout = go.Layout(title='Average Min and Max Temperatures by Month', xaxis_title='Average Min Temperature', yaxis_title='Average Max Temperature', hovermode='closest')

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubblechart.html')