import pandas as pd
from pandas.io.formats import style
from pandas_datareader import data as pdr
from datetime import datetime as date
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import plotly.express as px
import yfinance as yf
from dash.exceptions import PreventUpdate
from model import predict
from plotly.graph_objects import Layout
from plotly.validator_cache import ValidatorCache
app = dash.Dash()

def get_stock_price_fig(df):
    fig = px.line(df,x= "Date" ,y= ["Close","Open"], title="Closing and Opening Price vs Date",markers=True)
    fig.update_layout(title_x=0.5)
    return fig

def get_more(df):
    df['EWA_20'] = df['Close'].ewm(span=20, adjust=False).mean()
    fig = px.scatter(df,x= "Date",y= "EWA_20",title="Exponential Moving Average vs Date")
    fig.update_traces(mode= "lines+markers")
    return fig
