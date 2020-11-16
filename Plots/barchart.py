import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Olympic2016Rio.csv')

# Filtering US Cases
#filtered_df = df[df['NOC'] == 'US']

# Removing empty spaces from State column to avoid errors
#filtered_df = filtered_df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Creating sum of number of medals group by NOC Column
new_df = df.groupby(['NOC'])['Total'].sum().reset_index()

# Sorting values and select first 20 Countries
new_df = new_df.sort_values(by=['Total'], ascending=[False]).head(20)

# Preparing data
data = [go.Bar(x=new_df['NOC'], y=new_df['Total'])]

# Preparing layout
layout = go.Layout(title='Top 20 Countries Olympic 2016 Total Medals', xaxis_title="Country",
                   yaxis_title="Number of Medals")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='barchart.html')
