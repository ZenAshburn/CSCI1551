from direct.showbase.ShowBase import ShowBase
from panda3d.core import Loader, NodePath, Vec3
from direct.task import Task

class Universe(ShowBase):

    def __init__(self, loader:Loader, modelPath:str, parentNode:NodePath, nodeName:str, texPath:str, posVec:Vec3, scaleVec:float):

        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex,1)

class Planet(ShowBase):

    def __init__(self, loader:Loader, modelPath:str, parentNode:NodePath, nodeName:str, texPath:str, posVec:Vec3, scaleVec:float):

        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex,1)

class Dumbledore(ShowBase):

    def __init__(self, loader:Loader, modelPath:str, parentNode:NodePath, nodeName:str, texPath:str, posVec:Vec3, scaleVec:float):

        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex,1)

class SpaceStation(ShowBase):

    def __init__(self, loader:Loader, modelPath:str, parentNode:NodePath, nodeName:str, texPath:str, posVec:Vec3, scaleVec:float):

        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex,1)

class Drone(ShowBase):

    def __init__(self, loader:Loader, modelPath:str, parentNode:NodePath, nodeName:str, texPath:str, posVec:Vec3, scaleVec:float):

        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex,1)

    droneCount = 0
