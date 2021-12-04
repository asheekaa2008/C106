import plotly.express as px
import csv
with open('data1.csv')as f:
    df=csv.DictReader(f)
    figure=px.scatter(df,x='Temperature',y='IceCreamSales')
    figure.show()