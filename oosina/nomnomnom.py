from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader

app = Ursina()

Entity.default_shader = lit_with_shadows_shader

ground = Entity(model='plane', collider='box', scale=64, texture='grass')
player = FirstPersonController(model="cube", color=color.red, texture="shore", origin_y=-.5,z=-10)

# the default camera_pivot is (0,2,0)
player.camera_pivot.z = -3.5  # move the camera behind the player model
player.camera_pivot.y = 2.5  # move the camera a little higher

player.jump_height = 5

# setting collider and making it visible for debugging
player.collider = BoxCollider(player, Vec3(0,1,0), Vec3(1,2,1))
player.collider.visible=True

# adding some objects to collide with
#for i in range(600):
    #Entity(model='cube', origin_y=-.5, scale=2, texture='brick', texture_scale=(1,2),
        #x=random.uniform(-25,25),
        #z=random.uniform(-25,25) + 8,
        #y=random.uniform(0,8),
        #collider='box',
        #scale_y = random.uniform(2,3),
        #scale_y = (2),
        #color=color.hsv(0, 0, random.uniform(.9, 1))
    #)

#for i in range(600):
    #Entity(model='cube', origin_y=-.5, scale=2, texture='file_icon', texture_scale=(1,2),
        #x=random.uniform(-25,25),
        #z=random.uniform(-25,25) + 8,
        #y=random.uniform(9,16),
        #collider='box',
        #scale_y = random.uniform(2,3),
        #scale_y = (2),
        #color=color.hsv(0, 0, random.uniform(.9, 1))
    #)

#for i in range(400):
    #Entity(model='cube', origin_y=-.5, scale=2, texture='folder', texture_scale=(1,2),
        #x=random.uniform(-25,25),
        #z=random.uniform(-25,25) + 8,
        #y=random.uniform(17,24),
        #collider='box',
        #scale_y = random.uniform(2,3),
        #scale_y = (2),
        #color=color.hsv(0, 0, random.uniform(.9, 1))
    #)

#for i in range(300):
    #Entity(model='cube', origin_y=-.5, scale=2, texture='cobblestone', texture_scale=(1,2),
        #x=random.uniform(-25,25),
        #z=random.uniform(-25,25) + 8,
        #y=random.uniform(17,24),
        #collider='box',
        #scale_y = random.uniform(2,3),
        #scale_y = (2),
        #color=color.hsv(0, 0, random.uniform(.9, 1))
    #)

#model_name = load_model('ursina_test.glb')
entity = Entity(model='oosina/test.glb', scale=1, position=(0,0,0), rotation=(0,0,0))

sun = DirectionalLight()
sun.look_at(Vec3(1,-1,-1))
Sky()

def input(key):
    if key == 'q':
        exit()
    
app.run()