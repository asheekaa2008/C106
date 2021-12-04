import plotly.express as px
import csv
import numpy as np
def getDataSource(data_path):
    temperature=[]
    coldrinksales=[]
    with open(data_path) as f:
        csvReader=csv.DictReader(f)
        for row in csvReader:
            temperature.append(float(row["Temperature"]))
            coldrinksales.append(float(row["ColdDrinkSales"]))
    return{"x":temperature,"y":coldrinksales}
def findCorrelation(dataSource):
    Correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print(Correlation[0,1])
def setup():
    data_path='data1.csv'
    dataSource=getDataSource(data_path)
    findCorrelation(dataSource)
setup()
