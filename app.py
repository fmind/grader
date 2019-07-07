#!/usr/bin/env python3

"""Render a dashboard for students."""

import dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output

import plotly_express as px
import pandas as pd

STYLESHEETS = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

APP = dash.Dash(__name__, external_stylesheets=STYLESHEETS)

RECORDS = pd.read_json('datasets/records.jsonlines.gz', lines=True)

RECORDS = RECORDS[[
    'full_name', 'age', 'gender', 'nationality', 'academic_degree', 'university',
    'french', 'english', 'music', 'maths', 'physics', 'biology',
]]

OPTIONS = [
    {'label': 'french', 'value': 'french'},
    {'label': 'english', 'value': 'english'},
    {'label': 'music', 'value': 'music'},
    {'label': 'maths', 'value': 'maths'},
    {'label': 'physics', 'value': 'physics'},
    {'label': 'biology', 'value': 'biology'},
]


APP.layout = html.Div([
        html.H1('Student grades'),
        dcc.Markdown('## Powered by *Dash*'),
        html.H3('Tables'),
        dcc.Slider(
            id='nrows-slider',
            min=0,
            max=20,
            value=10,
            marks={str(i): str(i) for i in range(0, 20+1)},
        ),
        html.Div(id='record-table'),
        html.H3(children='Histogram'),
        dcc.Dropdown(
            id='hist-grade',
            value='french',
            options=OPTIONS,
        ),
        html.Div(id='hist-plot'),
        html.H3(children='Scatter plot'),
        dcc.Dropdown(
            id='scatter-x',
            value='french',
            options=OPTIONS,
        ),
        dcc.Dropdown(
            id='scatter-y',
            value='english',
            options=OPTIONS,
        ),
        html.Div(id='scatter-plot'),
    ],
)


@APP.callback(
    Output('hist-plot', 'children'),
    [Input('hist-grade', 'value')],
)
def generate_hist(grade):
    """Generate a histogram component."""
    return dcc.Graph(
        id='hist',
        figure=px.histogram(RECORDS, x=grade)
    )

@APP.callback(
    Output('scatter-plot', 'children'),
    [Input('scatter-x', 'value'),
     Input('scatter-y', 'value')],
)
def generate_scatter(x_grade, y_grade):
    """Generate a scatter component."""
    return dcc.Graph(
        id='scatter',
        figure=px.scatter(
            RECORDS,
            x=x_grade,
            y=y_grade,
            color='academic_degree',
        )
    )


@APP.callback(
    Output('record-table', 'children'),
    [Input('nrows-slider', 'value')],
)
def generate_table(nrows):
    """Generate a table component."""
    return html.Table(
        # head
        [html.Tr([html.Th(col) for col in RECORDS.columns])] +
        # body
        [html.Tr(
            [html.Td(val) for val in row.values]) \
            for _, row in RECORDS.head(nrows).iterrows()
        ]
    )


if __name__ == '__main__':
    APP.run_server(debug=True)
