import dash
from datetime import datetime as dt
import pandas as pd
import numpy as np

from plotly import graph_objs as go
from plotly.graph_objs import *
#import pandas_datareader as pdr
from dash.dependencies import Input
from dash.dependencies import Output

import os
basedir = os.path.abspath(os.path.dirname(__file__))



#    SQLALCHEMY_DATABASE_URI =     SECRET_KEY = os.environ['SECRET_KEY']

'''
File to upload the callbacks of the dashapp, this functions and callbacks are what give the 
functionality to the website app, all the buttons and dropdowns 

'''

"""
This function came with the sample code of the github repo
def register_callbacks(dashapp):
    @dashapp.callback(Output('my-graph', 'figure'), [Input('my-dropdown', 'value')])
    def update_graph(selected_dropdown_value):
        df = pdr.get_data_yahoo(selected_dropdown_value, start=dt(2017, 1, 1), end=dt.now())
        return {
            'data': [{
                'x': df.index,
                'y': df.Close
            }],
            'layout': {'margin': {'l': 40, 'r': 0, 't': 20, 'b': 30}}
        }
"""

mapbox_access_token = os.environ.get('mapbox_access_token')

data_path = r'/home/sebas-pc/documentos/marketing/dash_on_flask/app/marketing/assets/merged.csv'
df = pd.read_csv(data_path)
df1 = df.copy()

list_of_locations = df['Dpto Domicilio'].unique().tolist()
list_of_industries = df['Actividad CIIU'].unique().tolist()


# Update the total number of rides in selected times, all the names are from the dash gallery
# TODO: Change all the names of the buttons and id of the layouts to improve readability
def register_callbacks(app):
    '''
    Function to register all the callbacks, from here all the functions defining the behavior from the 
    dash app are coded
    '''
    @app.callback(
        Output("total-rides-selection", "children"),
        [Input("location-dropdown", "value"), Input("ind-selector", "value")],
    )
    def update_total_rides_selection(departamento, industria):
        num_business = df[(df['Dpto Domicilio'] == departamento) & (df['Actividad CIIU'] == industria)]['NIT'].count()
        firstOutput = "Numero total de empresas seleccionadas: {}".format(num_business)
        return "" # firstOutput


    # Update Map Graph based on date-picker, selected data on histogram and location dropdown
    @app.callback(
        Output("map-graph", "figure"),
        [
    #         Input("date-picker", "date"),
            Input("ind-selector", "value"),
            Input("location-dropdown", "value"),
        ],
    )
    def update_graph(industria, departamento):
        zoom = 4.5
        lat=7
        lon=-75.566293
        bearing = 0
        if industria != None and departamento != None:
            df1 = df[(df['Actividad CIIU'] == industria) & (df['Dpto Domicilio'] == departamento)]
        elif industria != None:
            df1 = df[df['Actividad CIIU'] == industria]
        elif departamento != None:
            df1 = df[df['Dpto Domicilio'] == departamento]
        else:
            df1 = df

        return go.Figure(
            data=[
                # Data for business depending on industry and department
                 go.Densitymapbox(
                    lat=df1.lat,
                    lon=df1.lon,
                    radius = 10,
                    hovertemplate='Ciudad: %{text}<extra></extra>',
                    text=[x for x in df1['Ciudad Domicilio']],
    #                 hoverinfo= 'text',

                ),
            ],
            layout=Layout(
                autosize=True,
                hovermode='closest',
                mapbox_style="dark",
                margin=go.layout.Margin(l=0, r=35, t=0, b=0),
                showlegend=False,
                mapbox=dict(
                    accesstoken=mapbox_access_token,
                    center=dict(lat=lat, lon=lon),  # 40.7272  # -73.991251
                    style="dark",
                    bearing=bearing,
                    zoom=zoom,
                ),
            ),
        )
