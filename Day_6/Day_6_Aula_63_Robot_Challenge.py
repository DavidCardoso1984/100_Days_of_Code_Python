def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while at_goal() is False:
    if wall_in_front() is True:
        jump()
    else:
        move()

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
