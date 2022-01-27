def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while front_is_clear():
        move()
    
while at_goal() is False: 
    if  not wall_in_front():
           move()
           if not wall_on_right():
              turn_right()
    elif not wall_on_right():       
           turn_right()
           move()
    elif  not front_is_clear():
           turn_left()
           

 

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
