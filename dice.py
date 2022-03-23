import random
import plotly.express as px
import plotly.figure_factory as pff

diceResult = []
count = []
for i in range(0,100):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    diceResult.append(dice1+dice2)
    count.append(i)
print(diceResult)

#fig = px.bar(x= diceResult, y= count)
#create a distplot, the label for it and both of them must be in list[] format
fig = pff.create_distplot([diceResult],["result"])
fig.show()