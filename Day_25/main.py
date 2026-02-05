import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
image = r"./Day_25/blank_states_img.gif"
screen.addshape(image)

data = pandas.read_csv(r"./Day_25/50_states.csv")
all_states = data.state.to_list()
x_cor = data.x.to_list()
y_cor = data.y.to_list()

turtle.shape(image)
turtle.penup()

guessed_states =[]
learn_states = data.state.to_list()
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",prompt="What's another state's name?").title()
    
    if answer_state == "Exit":
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        learn_states.remove(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        index = all_states.index(answer_state)
        current_x=x_cor[index]
        current_y=y_cor[index]
        t.goto((current_x-20,current_y))
        t.write(answer_state)

        
        
new_data = pandas.DataFrame(learn_states)
new_data.to_csv(r"./Day_25/states_to_learn.csv")


turtle.mainloop()
