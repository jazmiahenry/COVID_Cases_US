import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


app = dash.Dash(__name__)

df = pd.read_csv('US_Covid.csv')

df['submission_date'] = pd.to_datetime(df['submission_date'])

app.layout = html.Div(children=[
                      html.Div(className='row',  # Define the row element
                               children=[
                                  html.Div(className='two columns'),  # Define the left element
                                  html.Div(className='three columns'),  # Define the right element
    							  html.H2('COVID Cases in the US'),
    							  html.P('''Interactive Visualization of COVID Cases in the US'''),
    							  html.P('''Choose Your Visualization''')
])
                                ])

dcc.Graph(id='timeseries',
          config={'displayModeBar': False},
          animate=True,
          figure = px.scatter(df, x = 'submission_date'
          	, y = 'tot_cases', color = 'state').update_layout(
          	title = 'Total Covid Cases Over Time'
            , yaxis_title = 'Total Cases'
            , xaxis_title = 'Date'))


if __name__ == '__main__':
    app.run_server(debug=True)