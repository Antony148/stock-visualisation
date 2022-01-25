def predict(stock,days_n):
    from model import predict
    import pandas as pd
    from pandas.io.formats import style
    from pandas_datareader import data as pdr
    from datetime import datetime as date
    from datetime import timedelta
    import dash
    import dash_core_components as dcc
    import dash_html_components as html
    from dash.dependencies import Input, Output, State
    import plotly.graph_objs as go
    import plotly.express as px
    import yfinance as yf
    from dash.exceptions import PreventUpdate
    from sklearn.model_selection import GridSearchCV
    from sklearn.svm import SVR
    from sklearn.model_selection import train_test_split
