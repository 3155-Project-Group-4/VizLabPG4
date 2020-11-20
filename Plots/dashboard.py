import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df1 = pd.read_csv('../Datasets/CoronavirusTotal.csv')
df2 = pd.read_csv('../Datasets/CoronaTimeSeries.csv')

app = dash.Dash()

# Bar chart data
# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Olympic2016Rio.csv')
df4 = pd.read_csv('../Datasets/Weather2014-15.csv')
# Sorting values and select first 20 countries
new_df = df.sort_values(by=['Total'], ascending=[False]).head(20)

# Preparing data
data_barchart = [go.Bar(x=new_df['NOC'], y=new_df['Total'])]


# Stack bar chart data
df = pd.read_csv('../Datasets/Olympic2016Rio.csv')

# Sort and select top 20
new_df = df.sort_values(by=['Total'], ascending=[False]).head(20).reset_index()

# Prepare data
trace_1 = go.Bar(x=new_df['NOC'], y=new_df['Bronze'], name='Bronze', marker={'color': '#e07b39'})
trace_2 = go.Bar(x=new_df['NOC'], y=new_df['Silver'], name='Silver', marker={'color': '#AFAFAF'})
trace_3 = go.Bar(x=new_df['NOC'], y=new_df['Gold'], name='Gold', marker={'color': '#F9FF42'})
data_stackbarchart = [trace_1, trace_2, trace_3]



# Line Chart
df = pd.read_csv('../Datasets/Weather2014-15.csv')
df['date'] = pd.to_datetime(df['date'])

new_df = df.groupby(df['date'].dt.month)
maxs_df = new_df.max()
# maxs_df = maxs_df.reset_index()

# Prepare data
data_linechart = [go.Scatter(x=maxs_df['date'].dt.month_name(), y=maxs_df['actual_max_temp'], mode='lines', name='Max Temps')]



# Multi Line Chart
df = pd.read_csv('../Datasets/Weather2014-15.csv')
df['date'] = pd.to_datetime(df['date'])

# max df
new_df = df.groupby(df['date'].dt.month)
maxs_df = new_df.max()


# min df
min_df = new_df.min()

# mean df
mean_df = new_df.mean()


# Prepare data
trace1 = go.Scatter(x=maxs_df['date'].dt.month_name(), y=maxs_df['actual_max_temp'], mode='lines', name='Max Temps')
trace2 = go.Scatter(x=min_df['date'].dt.month_name(), y=min_df['actual_min_temp'], mode='lines', name='Min Temps')
trace3 = go.Scatter(x=maxs_df['date'].dt.month_name(), y=mean_df['actual_mean_temp'], mode='lines', name='Mean Temps')
data_multiline = [trace1, trace2, trace3]



# Bubble chart
bubble_df = df4.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

bubble_df = bubble_df.groupby(['date']).agg(
    { 'average_max_temp': 'sum', 'average_min_temp': 'sum'}).reset_index()
data_bubblechart = [
    go.Scatter(x=bubble_df['average_min_temp'],
               y=bubble_df['average_max_temp'],
               text=bubble_df['date'],

               mode='markers',
               marker=dict(size=bubble_df['average_max_temp'], color=bubble_df['average_max_temp'], showscale=True))
]


# Heatmap
# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')

# Preparing data
data_heatmap = [go.Heatmap(x=df['day'],
                   y=df['month'],
                   z=df['actual_max_temp'].values.tolist(),
                   colorscale='Jet')]

# Layout
app.layout = html.Div(children=[
    html.H1(children='Python Dash',
            style={
                'textAlign': 'center',
                'color': '#ef3e18'
            }
            ),
    html.Div('Web dashboard for Data Visualization using Python', style={'textAlign': 'center'}),
    html.Div('2016 Olympics and 2014-2015 weather data', style={'textAlign': 'center'}),
    html.Br(),
    html.Br(),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Interactive Bar chart', style={'color': '#df1e56'}),
    html.Div('This bar chart represent the number of confirmed cases in the first 20 countries of selected continent.'),
    dcc.Graph(id='graph1'),
    html.Div('Please select a continent', style={'color': '#ef3e18', 'margin':'10px'}),
    dcc.Dropdown(
        id='select-continent',
        options=[
            {'label': 'Asia', 'value': 'Asia'},
            {'label': 'Africa', 'value': 'Africa'},
            {'label': 'Europe', 'value': 'Europe'},
            {'label': 'North America', 'value': 'North America'},
            {'label': 'Oceania', 'value': 'Oceania'},
            {'label': 'South America', 'value': 'South America'}
        ],
        value='Europe'
    ),
    html.Br(),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Bar chart', style={'color': '#df1e56'}),
    html.Div('This bar chart represent the Total Medals won in the 2016 Olympics of the first 20 countries.'),
    dcc.Graph(id='graph2',
              figure={
                  'data': data_barchart,
                  'layout': go.Layout(title='Total Medals won in the 2016 Olympics', xaxis_title="Country",
                   yaxis_title="Total Medals won")

              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Stack bar chart', style={'color': '#df1e56'}),
    html.Div(
        'This stack bar chart represent the Number of medals awarded to the top 20 countries in the 2016 Olympics.'),
    dcc.Graph(id='graph3',
              figure={
                  'data': data_stackbarchart,
                  'layout': go.Layout(title="Number of medals awarded to the top 20 countries in the 2016 Olympics", xaxis_title='Country', yaxis_title='Number of Medals', barmode='stack')
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Line chart', style={'color': '#df1e56'}),
    html.Div('This line chart represent the 2014-2015 Max Temps By Month'),
    dcc.Graph(id='graph4',
              figure={
                  'data': data_linechart,
                  'layout': go.Layout(title='2014-2015 Max Temps By Month', xaxis_title='Month', yaxis_title='Temperature')
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Multi Line chart', style={'color': '#df1e56'}),
    html.Div(
        'This line chart represent the Max, Min, and Mean Temp by Month (2014-2015).'),
    dcc.Graph(id='graph5',
              figure={
                  'data': data_multiline,
                  'layout': go.Layout(title='Max, Min, and Mean Temp by Month (2014-2015)', xaxis_title='Temperature', yaxis_title='Month')
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Bubble chart', style={'color': '#df1e56'}),
    html.Div(
        'This bubble chart represent the average minimum and maximum temperature for the given dates.'),
    dcc.Graph(id='graph6',
              figure={
                  'data': data_bubblechart,
                  'layout': go.Layout(title='Average Temperatures',
                                      xaxis={'title': 'Min Temp'}, yaxis={'title': 'Max Temp'},
                                      hovermode='closest')
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Heat map', style={'color': '#df1e56'}),
    html.Div(
        'This heat map represent the Record max Temperature by month.'),
    dcc.Graph(id='graph7',
              figure={
                  'data': data_heatmap,
                  'layout': go.Layout(title='Record max Temperature', xaxis_title="Day",
                   yaxis_title="Month")
              }
              )
])


@app.callback(Output('graph1', 'figure'),
              [Input('select-continent', 'value')])
def update_figure(selected_continent):
    filtered_df = df1[df1['Continent'] == selected_continent]

    filtered_df = filtered_df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    new_df = filtered_df.groupby(['Country'])['Confirmed'].sum().reset_index()
    new_df = new_df.sort_values(by=['Confirmed'], ascending=[False]).head(20)
    data_interactive_barchart = [go.Bar(x=new_df['Country'], y=new_df['Confirmed'])]
    return {'data': data_interactive_barchart, 'layout': go.Layout(title='Corona Virus Confirmed Cases in '+selected_continent,
                                                                   xaxis={'title': 'Country'},
                                                                   yaxis={'title': 'Number of confirmed cases'})}


if __name__ == '__main__':
    app.run_server()