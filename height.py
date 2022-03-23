import pandas as pd 
import plotly.figure_factory as pff

dataframe = pd.read_csv("data.csv")
x = dataframe["Height(Inches)"].tolist()
#print(x)
fig = pff.create_distplot([dataframe["Height(Inches)"].tolist()],["Height of 18 year olds"],show_hist = False)
fig.show()