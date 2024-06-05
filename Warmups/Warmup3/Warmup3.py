from direct.showbase.ShowBase import ShowBase 
from panda3d.core import CollisionTraverser, CollisionHandlerPusher
from panda3d.core import CollisionNode, CollisionSphere
import random
import math
import sys

class MyApp(ShowBase):

    def __init__(self):
        
        ShowBase.__init__(self)
        self.fighter = self.loader.loadModel('./Assets/sphere')
        self.fighter.reparentTo(self.render)
        self.fighter.setColorScale(1.0, 0.0, 0.0, 1.0)

        self.parent = self.loader.loadModel("./Assets/cube")

        self.parentCnode = self.parent.attachNewNode(CollisionNode('pcnode'))
        self.parentCnode.node().addSolid(CollisionSphere(0, 0, 0, 1.8))
        self.fighterCnode = self.fighter.attachNewNode(CollisionNode('fcnode'))
        self.fighterCnode.node().addSolid(CollisionSphere(0, 0, 0, 1.8))
        self.traverser = CollisionTraverser()
        self.traverser.traverse(self.render)
        self.pusher = CollisionHandlerPusher()
        self.pusher.addCollider(self.fighterCnode, self.fighter)
        self.pusher.addCollider(self.parentCnode, self.parent)
        self.traverser.addCollider(self.fighterCnode, self.pusher)
        self.traverser.showCollisions(self.render)
        self.parentCnode.show()
        self.fighterCnode.show()

        x = 0
        for i in range(100):
            theta = x
            self.placeholder2 = self.render.attachNewNode('Placeholder2')
            self.placeholder2.setPos(50.0 * math.cos(theta), 50.0 * math.sin(theta), 0.0 * math.tan(theta))
            red = 0.6 + random.random() * 0.4
            green = 0.6 + random.random() * 0.4
            blue = 0.6 + random.random() * 0.4
            self.placeholder2.setColorScale(red, green, blue, 1.0)
            self.parent.instanceTo(self.placeholder2)
            x = x + 0.06

        self.accept('escape', self.quit)
        
        self.disableMouse()

        self.camera.setPos(0.0, 0.0, 250.0)
        self.camera.setHpr(0.0, -90.0, 0.0)

        self.accept('arrow_left', self.negativeX, [1])
        self.accept('arrow_left-up', self.negativeX, [0])

        self.accept('arrow_right', self.positiveX, [1])
        self.accept('arrow_right-up', self.positiveX, [0])

        self.accept('arrow_down', self.negativeY, [1])
        self.accept('arrow_down-up', self.negativeY, [0])

        self.accept('arrow_up', self.positiveY, [1])
        self.accept('arrow_up-up', self.positiveY, [0])

    def quit(self):
        sys.exit()

    def negativeX(self, keyDown):
        if (keyDown):
            self.taskMgr.add(self.moveNegativeX, 'moveNegativeX')
        else:
            self.taskMgr.remove('moveNegativeX')

    def moveNegativeX(self, task):
        self.fighter.setX(self.fighter, -1)
        return task.cont
    
    def positiveX(self, keyDown):
        if (keyDown):
            self.taskMgr.add(self.movePositiveX, 'movePositiveX')
        else:
            self.taskMgr.remove('movePositiveX')

    def movePositiveX(self, task):
        self.fighter.setX(self.fighter, 1)
        return task.cont
    
    def negativeY(self, keyDown):
        if (keyDown):
            self.taskMgr.add(self.moveNegativeY, 'moveNegativeY')
        else:
            self.taskMgr.remove('moveNegativeY')

    def moveNegativeY(self, task):
        self.fighter.setY(self.fighter, -1)
        return task.cont
    
    def positiveY(self, keyDown):
        if (keyDown):
            self.taskMgr.add(self.movePositiveY, 'movePositiveY')
        else:
            self.taskMgr.remove('movePositiveY')

    def movePositiveY(self, task):
        self.fighter.setY(self.fighter, 1)
        return task.cont


app = MyApp()
app.run()