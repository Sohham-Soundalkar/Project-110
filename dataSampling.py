import plotly.figure_factory as pf
import plotly.graph_objects as pg
import statistics as st
import pandas as pd
import random
import csv

df = pd.read_csv('medium_data.csv')
data = df['reading_time'].tolist()

populationMean = st.mean(data)
print('populationMean: ', populationMean)
standardDeviation = st.stdev(data)
print('standardDeviationMean: ', standardDeviation)
graph = pf.create_distplot([data],['reading_time'])
# graph.show()

dataset = []
for i in range(0,100):
    randomEntries = random.randint(0,len(data))
    value = data[randomEntries]
    dataset.append(value)

sampleMean = st.mean(dataset)
print('sampleMean: ', sampleMean)
sampleSD = st.stdev(dataset)
print('sampleSD: ', sampleSD)

def randomMean(counter):
    dataset = []
    for i in range(0,counter):
        randomEntries = random.randint(0,len(data)-1)
        value = data[randomEntries]
        dataset.append(value)

    mean = st.mean(dataset)
    return mean

def createGraph(meanList):
    df = meanList
    mean = st.mean(df)
    graph = pf.create_distplot([df],['reading_time'],show_hist=False)
    graph.add_trace(pg.Scatter(x=[mean, mean], y=[0,1], mode='lines', name = 'Mean'))
    graph.show()

def setup():
    meanList = []
    for i in range(0,1000):
        setOfMeans = randomMean(100)
        meanList.append(setOfMeans)

    createGraph(meanList)
    mean = st.mean(meanList)
    print('finalMeanofSample: ', mean)

def setupSD():
    SDList = []
    for i in range(0,1000):
        setOfSD = randomMean(100)
        SDList.append(setOfSD)

    SD = st.stdev(SDList)
    print('finalSDofSample: ', SD)

setup()
setupSD()