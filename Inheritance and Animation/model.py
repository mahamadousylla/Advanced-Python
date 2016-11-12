import controller, sys
import model   #strange, but we need a reference to this module to pass this module to update

from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter
from Special import Special


# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running = False
cycle_count = 0
balls = set()
for_step = False
the_object = ''

#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running,cycle_count, balls, for_step
    running = False
    cycle_count = 0
    balls = set()
    for_step = False


#start running the simulation
def start ():
    global running
    running = True


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False


#step just 1 update in the simulation
def step ():
    global running, for_step
    running = True
    for_step = True


#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global the_object
    the_object = kind


#add the kind of remembered object to the simulation (or remove any objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    global balls, the_object
    if the_object.lower() == 'remove':
        all_found = find(lambda ball: ball.contains( (x,y) ))
        for ball in all_found:
            balls.remove(ball)
    else:
        balls.add(eval(the_object + '(' + str(x) + ',' + str(y) + ')'))
        


#add simulton s to the simulation
def add(s):
    global balls
    balls.add(s)
    

# remove simulton s from the simulation    
def remove(s):
    global balls
    balls.discard(s)
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    return {i for i in balls if p(i)}
#     s = set()
#     for i in balls:
#         if p(i):
#             s.add(i)
#     return s


#call update for every simulton in the simulation
def update_all():
    global cycle_count, running, for_step, balls
    if running is True:
        cycle_count += 1
        new_balls = balls.copy()
        all_balls = [ball.update(model) for ball in new_balls if ball in balls]
        if for_step is True:
            running = False
            for_step = False


#delete from the canvas every simulton in the simulation, and then call display for every
#  simulton in the simulation to add it back to the canvas possibly in a new location: to
#  animate it; also, update the progress label defined in the controller
def display_all():
    for i in controller.the_canvas.find_all():
        controller.the_canvas.delete(i)
    
    for ball in balls:
        ball.display(controller.the_canvas)
    
    controller.the_progress.config(text = str(len(balls)) +" balls/" + str(cycle_count) + " cycles")
