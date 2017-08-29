#!/usr/bin/python
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import pandas as pd
from plotly.graph_objs import Scatter, Figure, Layout
import sys

#S0      Survivor space 0 utilization as a percentage of the space's current capacity.
#S1      Survivor space 1 utilization as a percentage of the space's current capacity.
#E       Eden space utilization as a percentage of the space's current capacity.
#O       Old space utilization as a percentage of the space's current capacity.
#P       Permanent space utilization as a percentage of the space's current capacity.

#YGC	Number of young generation GC Events.
#YGCT	Young generation garbage collection time.
#FGC	Number of full GC events.
#FGCT	Full garbage collection time.
#GCT	Total garbage collection time.

def openFile(file):
    newfile = open(file + "_cleaned", 'w')
    newfile.write('Date Time S0     S1     E      O      P     YGC     YGCT    FGC    FGCT     GCT')
    # remove rows containing "S0     S1     E      O      P     YGC     YGCT    FGC    FGCT     GCT"
    with open(file) as oldfile:
        for line in oldfile:
            if not  "S0     S1     E      O      P     YGC     YGCT    FGC    FGCT     GCT" in line:
                newfile.write(line)

    newfile.close()
    return;


def createDataFrame(file):
    df = pd.read_csv(file + "_cleaned", delimiter=r"\s+")
    df["FullDate"] = df["Date"]+ '.' + df["Time"]
    df['FullDate'] = pd.to_datetime(df['FullDate'], format="%d.%m.%y.%H:%M:%S:")
    return df;


#Memory utilization graph
def createMemoryUtilizationGraph(df):
    #print df
    #print df.dtypes
    traceS0 = Scatter(
        x=df.FullDate,
        y=df.S0, name = "Survivor space 0 utilization as a percentage of the space's current capacity.")

    #Memory utilization plot
    traceS1 = Scatter(
        x=df.FullDate,
        y=df.S1, name = "Survivor space 1 utilization as a percentage of the space's current capacity.")

    traceP = Scatter(
              x=df.FullDate,
              y=df.P, name = "Permanent space utilization as a percentage of the space's current capacity.")

    traceE = Scatter(
        x=df.FullDate,
        y=df.E, name = "Eden space utilization as a percentage of the space's current capacity.")

    traceO = Scatter(
        x=df.FullDate,
        y=df.O, name = " Old space utilization as a percentage of the space's current capacity.")

    data =[ traceS0, traceS1, traceE, traceO, traceP]
    layout = Layout(
        showlegend=True
    )
    fig = Figure(data=data, layout=layout)
    plot(fig)





#Garbage collection events graph
def createGCEventsGraph(df):
    traceYGC = Scatter(
        x=df.FullDate,
        y=df.YGC, name = 'Number of young generation GC Events.')


    traceFGC = Scatter(
        x=df.FullDate,
        y=df.FGC, name = 'Number of full GC events.')

    dataGCEvents = [traceYGC, traceFGC]
    layout = Layout(
        showlegend=True
    )
    figGCEvents = Figure(data=dataGCEvents, layout=layout)
    plot(figGCEvents)


#Garbage collection time graph
def createGCTimeGraph(df):
    traceYGCT = Scatter(
        x=df.FullDate,
        y=df.YGCT, name = 'Young generation garbage collection time.')


    traceFGCT = Scatter(
        x=df.FullDate,
        y=df.FGCT, name = 'Full garbage collection time.',)


    dataGCTime = [traceYGCT, traceFGCT]
    layout = Layout(
        showlegend=True
    )
    figGCTime = Figure(data=dataGCTime, layout=layout)
    plot(figGCTime)



print sys.argv

if(len(sys.argv) != 2):
    print "Expected usage: \n  python jstat-graph.py filename"
    sys.exit()

file = sys.argv[1]
openFile(file)
df = createDataFrame(file)
createMemoryUtilizationGraph(df)
createGCEventsGraph(df)
createGCTimeGraph(df)