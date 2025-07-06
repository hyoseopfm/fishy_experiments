from ursina import *

class MeshTerrain:
    def __init__(self):

        self.block = load_model('block.obj')
        self.textureatlas = 'pass'

        self.subsets = []
        self.numSubsets = 1
        self.subWidth = 32

        for i in range(0, self.numSubsets):
            e = Entity(model=self.block,
                       texture = self.textureatlas)
            self.subsets.append(e)

    def genTerrain(self):
