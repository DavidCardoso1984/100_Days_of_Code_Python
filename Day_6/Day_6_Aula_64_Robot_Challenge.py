def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    if wall_in_front() is True:
        turn_left()
    else:
        move()
        turn_right()

while at_goal() is False:
    if wall_in_front() is True:
        jump()
    else:
        move()
        turn_right()

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
