import random
import plotly.express as px
import plotly.figure_factory as ff

sumOfTwoDices=[]
scoresOnEachDice=[]

for i in range(0,100):
    firstDice=random.randint(1,6)
    secondDice=random.randint(1,6)
    scoresOnEachDice.append(firstDice+secondDice)
    sumOfTwoDices.append(i)

print(sumOfTwoDices,scoresOnEachDice)

fig=px.bar(x=sumOfTwoDices,y=scoresOnEachDice)
fig.show()

fig1=ff.create_distplot([scoresOnEachDice],["Sum"])
fig1.show()
