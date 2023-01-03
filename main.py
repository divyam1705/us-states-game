from turtle import Turtle,Screen
import pandas
s1=Screen()
s1.addshape("blank_states_img.gif")
t1=Turtle(shape="blank_states_img.gif")
t2=Turtle()
t2.pu()
t2.hideturtle()
states=pandas.read_csv("50_states.csv")
listofcoorx=states["x"].to_list()
listofcoory=states["y"].to_list()
listofstates=states["state"].to_list()
correctans=0
cstates=[]
missedstates=[]
while correctans<50:
    input1=s1.textinput(f"{correctans}/50 correct","GUESS THE STATE")
    if input1=="Exit":
        for i in listofstates:
            if i not in cstates:
                missedstates.append(i)
        x=pandas.Series(missedstates)
        x.to_csv("missedstates1byp")
        break
    for i in range(0,len(listofstates)):
        if input1.lower()==listofstates[i].lower():
            correctans+=1
            cstates.append(f"{listofstates[i]}")
            t2.goto(int(listofcoorx[i]),int(listofcoory[i]))
            t2.write(f"{listofstates[i]}")






s1.exitonclick()