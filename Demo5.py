import plotly.express as px
import csv
with open('data5.csv')as f:
    df=csv.DictReader(f)
    figure=px.scatter(df,x='RollNo',y='MarksInPercentage',color='DaysPresent')
    figure.show()