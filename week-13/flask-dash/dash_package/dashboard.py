import dash
import dash_core_components as dcc
import dash_html_components as html

from dash_package import app
from dash_package.functions import *

x = [1, 2, 3, 4, 5]

app.layout = html.Div(children=[
    html.H1(sayhello(), style={'color': 'red', 'font-family': 'verdana', 'textAlign': 'center'}),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': x, 'y': [twox(i) for i in x], 'type': 'bar', 'name': 'f1'},
                {'x': x[::-1], 'y': [half(i) for i in x], 'type': 'bar', 'name': 'f2'},
            ],
            'layout': {
                'title': title()
            }
        }
    )

])
