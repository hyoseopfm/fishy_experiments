from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

car = Entity(model="duck_car_actual.glb",
             position=(0,2,0),
             collider = 'box',
             scale=(1,1,1))

camera.parent = car
camera.position = (0,8,-26)
camera.rotation_x=12

class CarController(FirstPersonController):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.speed = 5
        self.rotation_speed = 100

    def update(self):
        # Handle movement based on input
        if held_keys['w']:
            self.position += self.forward * time.dt * self.speed
        if held_keys['s']:
            self.position -= self.forward * time.dt * self.speed
        if held_keys['a']:
            self.rotation_y += self.rotation_speed * time.dt
        if held_keys['d']:
            self.rotation_y -= self.rotation_speed * time.dt

car_controller = CarController()



window.color=color.blue



track_one_parent = Entity()
track=Entity(parent=track_one_parent, model='cube', color=color.green, scale=(10, .5, 60), position=(0,0), texture="road.png")
track_continued=Entity(parent=track_one_parent, model='cube', color=color.green, scale=(10, .5, 60), position=(0,0, 60), texture="road.png")
track_continued_end=Entity(parent=track_one_parent, model='cube', color=color.green, scale=(10,.5,60), position=(0,0, 120), texture="road.png")
track_one_parent.combine()


#EditorCamera()

app.run()
