################################################################################
# About
################################################################################

"""Entrypoint to the hello program."""

################################################################################
# Imports
################################################################################

import emoji

from . import starfish

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from mesh_terrain import MeshTerrain

################################################################################
# Entrypoint
################################################################################


def main() -> None:
    print(emoji.emojize('Hello, something is :fish:'))
    app = Ursina()

    player = FirstPersonController()
    ground = Entity(model='plane', collider='box', scale=64, texture='grass', texture_scale=(4,4))

    terrain = MeshTerrain()

    def update():
        #updateTerrain()


    terrain.genTerrain()

    app.run()


    #print("Hello, something's fishy...")
    #print(f"Hello, I am {starfish.bluey()}")
