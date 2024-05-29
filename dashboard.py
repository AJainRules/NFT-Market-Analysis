import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("NFT Market Trends Dashboard"),
    dcc.Graph(id='nft-sales'),
    dcc.Interval(id='interval-component', interval=1*60000, n_intervals=0)  # Update every minute
])

@app.callback(
    Output('nft-sales', 'figure'),
    [Input('interval-component', 'n_intervals')]
)
def update_graph(n):
    df = pd.read_csv('Users/apjain/Documents/NFT Project/NFTlyze Dataset.csv')  # Replace with real-time data fetching
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    df_sales = df['Sales_USD'].dropna()

    trace = go.Scatter(x=df_sales.index, y=df_sales, mode='lines', name='NFT Sales')
    return {'data': [trace], 'layout': go.Layout(title='NFT Sales Over Time')}

if __name__ == '__main__':
    app.run_server(debug=True)
