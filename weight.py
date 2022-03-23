import plotly.figure_factory as pff
import pandas as pd 

wireframe = pd.read_csv("data.csv")
fig = pff.create_distplot([wireframe["Weight(Pounds)"].tolist()], ["Weight of 18 year olds"], show_hist = False)
fig.show()