import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np


"""
Layout file to upload all the html components of the dash app with the format to include the
graphics and charts from the callbacks file
 
"""

data_path = r'/home/sebas-pc/documentos/marketing/dash_on_flask/app/marketing/assets/merged.csv'

df = pd.read_csv(data_path)
df1 = df.copy()

list_of_locations = df['Dpto Domicilio'].unique().tolist()
list_of_industries = df['Actividad CIIU'].unique().tolist()


"""
This layout was the sample code that came with the github repo
layout = html.Div([
    html.H1('Stock Tickers'),
    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'Coke', 'value': 'COKE'},
            {'label': 'Tesla', 'value': 'TSLA'},
            {'label': 'Apple', 'value': 'AAPL'}
        ],
        value='COKE'
    ),
    dcc.Graph(id='my-graph')
], style={'width': '500'})
"""


layout = html.Div(
    children=[
        html.Div(
            className="row",
            children=[
                # Column for user controls
                html.Div(
                    className="four columns div-user-controls",
                    children=[
                        html.H1("PROYECTO DE MARKETING DIGITAL"),
                        html.H2("Mapa empresarial en Colombia"),
                        html.P(
                            """Seleccione diferentes opciones de industrias y departamentos"""
                        ),
#                         html.Div(
#                             className="div-for-dropdown",
#                             children=[
#                                 dcc.DatePickerSingle(
#                                     id="date-picker",
#                                     min_date_allowed=dt(2014, 4, 1),
#                                     max_date_allowed=dt(2014, 9, 30),
#                                     initial_visible_month=dt(2014, 4, 1),
#                                     date=dt(2014, 4, 1).date(),
#                                     display_format="MMMM D, YYYY",
#                                     style={"border": "0px solid black"},
#                                 )
#                             ],
#                         ),
                        # Change to side-by-side for mobile layout
                        html.Div(
                            className="row",
                            children=[
                                html.Div(
                                    className="div-for-dropdown",
                                    children=[
                                        # Dropdown for locations on map
                                        dcc.Dropdown(
                                            id="location-dropdown",
                                            options=[
                                                {"label": i, "value": i}
                                                for i in list_of_locations
                                            ],
                                            placeholder="Seleccione un departamento",
                                        )
                                    ],
                                ),
                                html.Div(
                                    className="div-for-dropdown",
                                    children=[
                                        # Dropdown to select industries
                                        dcc.Dropdown(
                                            id="ind-selector",
                                            options=[
                                                {
                                                    "label": n, "value": n}
                                                for n in list_of_industries
                                            ],
#                                             multi=True,
                                            placeholder="Seleccione una industria",
                                        )
                                    ],
                                ),
                            ],
                        ),
                        html.P(id="total-rides"),
                        html.P(id="total-rides-selection"),
                        html.P(id="date-value"),
#                         dcc.Markdown(
#                             children=[
#                                 "Source: [FiveThirtyEight](https://github.com/fivethirtyeight/uber-tlc-foil-response/tree/master/uber-trip-data)"
#                             ]
#                         ),
                    ],
                ),
                # Column for app graphs and plots
                html.Div(
                    className="eight columns div-for-charts bg-grey",
                    children=[
                        dcc.Graph(id="map-graph"),
#                         html.Div(
#                             className="text-padding",
#                             children=[
#                                 "Select any of the bars on the histogram to section data by time."
#                             ],
#                         ),
#                         dcc.Graph(id="histogram"),
                    ],
                ),
            ],
        )
    ]
)