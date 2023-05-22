import dash_mantine_components as dmc
import plotly.express as px
from dash import dcc, html
from database import (CLIENT_NAME, ITEM, PERIOD_END, PERIOD_START, SHIFT_DAY,
                      df, percents)
from utils import create_timeline

CARD_STYLE = dict(withBorder=True,
                  shadow="sm",
                  radius="md",
                  style={'height': '500px'})

fig = create_timeline(df)


def get_layout():
    options = df['state'].unique()

    return html.Div([
        dmc.Paper([
            dmc.Grid([
                dmc.Col([
                    dmc.Card([
                        html.Div(f'Клиент: {CLIENT_NAME}',
                                 className='heading'),
                        html.Div(f'Сменный день: {SHIFT_DAY}',
                                 className='text_bold'),
                        html.Div(f'Точка учета: {ITEM}',
                                 className='text_bold'),
                        html.Div(f'Начало периода: {PERIOD_START}',
                                 className='text_bold'),
                        html.Div(f'Конец периода: {PERIOD_END}',
                                 className='text_bold'),
                        dcc.Dropdown(id='input-dropdown',
                                     options=[{'label': val, 'value': val}
                                              for val in options],
                                     multi=True),
                        dmc.Button(
                            'Фильтровать',
                            id='filter')],
                        **CARD_STYLE)
                ], span=6),
                dmc.Col([
                    dmc.Card([
                        html.Div('Статусы состояний', className='heading'),
                        dcc.Graph(figure=px.pie(values=percents.values(),
                                                names=percents.keys()),
                                  id="states",
                                  style={'margin-top': '20px',
                                         'margin-bottom': '10px'})],
                        **CARD_STYLE)
                ], span=6),
                dmc.Col([
                    dmc.Card([
                        html.Div('График состояний',
                                 className='heading_down'),
                        dcc.Graph(figure=fig, id='graph')],
                        **CARD_STYLE)
                ], span=12),
            ], gutter="xl", )
        ])
    ])
