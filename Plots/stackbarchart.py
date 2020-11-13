import pandas as pd
import plotly.offline as pyo
import plotly.graph_objects as go

# Load CSV
df = pd.read_csv('../Datasets/Olympic2016Rio.csv')

# Sort and select top 20
new_df = df.sort_values(by=['Total'], ascending=[False]).head(20).reset_index()

# Prepare data
trace_1 = go.Bar(x=new_df['NOC'], y=new_df['Bronze'], name='Bronze', marker={'color': '#e07b39'})
trace_2 = go.Bar(x=new_df['NOC'], y=new_df['Silver'], name='Silver', marker={'color': '#AFAFAF'})
trace_3 = go.Bar(x=new_df['NOC'], y=new_df['Gold'], name='Gold', marker={'color': '#F9FF42'})
data = [trace_1, trace_2, trace_3]

# Prepare Layout
layout = go.Layout(title="Number of medals awarded to the top 20 countries in the 2016 Olympics", xaxis_title='Country', yaxis_title='Number of Medals', barmode='stack')

# Plot the graph
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='stackbarchart.html')