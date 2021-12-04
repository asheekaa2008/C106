import plotly.express as px
import csv
import numpy as np
def getDataSource(data_path):
    RollNo=[]
    MarksInPercentage=[]
    DaysPresent=[]
    with open(data_path) as f:
        csvReader=csv.DictReader(f)
        for row in csvReader:
            RollNo.append(float(row["Roll no"]))
            MarksInPercentage.append(float(row["Marks%"]))
            DaysPresent.append(float(row["Days"]))

    return{"x":RollNo,"y":MarksInPercentage,"color":DaysPresent}
def findCorrelation(dataSource):
    Correlation=np.corrcoef(dataSource["x"],dataSource["y"],dataSource["color"])
    print(Correlation[0,1])
def setup():
    data_path='data5.csv'
    dataSource=getDataSource(data_path)
    findCorrelation(dataSource)
setup()
