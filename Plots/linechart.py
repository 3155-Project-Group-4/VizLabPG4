import pandas as pd
import plotly.offline as pyo
import plotly.graph_objects as go

# Load CSV
df = pd.read_csv('../Datasets/Weather2014-15.csv')
df['date'] = pd.to_datetime(df['date'])

new_df = df.groupby(df['date'].dt.month)
maxs_df = new_df.max()
# maxs_df = maxs_df.reset_index()

# Prepare data
data = [go.Scatter(x=maxs_df['date'].dt.month, y=maxs_df['actual_max_temp'], mode='lines', name='Max Temps')]
layout = go.Layout(title='2014-2015 Max Temps By Month', xaxis_title='Month', yaxis_title='Temperature')

# Plot the figure
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='linechart.html')