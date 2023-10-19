from grass import Grass
from boy import Boy

objects = [[],[]]
def add_object(o, depth=0):
    objects.append(o)

def add_objects(ol, depth=0):
    objects[depth] += ol


def update():
    for o in objects:
        o.update()
def render():
    for o in objects:
        o.draw()

def create_world(game_world=None):
    global running
    global grass
    global team
    global boy
    running = True
    grass = Grass()
    game_world.add_object(grass)
    boy = Boy()
    game_world.add_object(boy)

def update_world():
    for layer in objects:
        for o in layer:
            o.update()

def render_world():
    for layer in objects:
        for o in layer:
            o.draw()

def remove_object(o):
    for layer in objects:
        if o in layer:
            layer.remove(o)
            return
    raise ValueError('Cannot delete non existing object')
