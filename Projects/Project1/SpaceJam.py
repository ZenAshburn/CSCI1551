from direct.showbase.ShowBase import ShowBase
from panda3d.core import TextureStage

class MyApp(ShowBase):

    def __init__(self):
        
        ShowBase.__init__(self)
        self.SetupScene()

    def SetupScene(self):

        self.Universe = self.loader.loadModel("./Assets/Universe/Universe.x")
        self.Universe.reparentTo(self.render)
        self.Universe.setScale(15000)
        self.Universe.setHpr(173, 123, 37)
        tex = self.loader.loadTexture("./Assets/Universe/starfield-in-blue.jpg")
        self.Universe.setTexture(tex, 1)

        self.Planet1 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet1.reparentTo(self.render)
        self.Planet1.setPos(1720, 72, 1900)
        self.Planet1.setHpr(146, 19, 1)
        self.Planet1.setScale(150)
        tex = self.loader.loadTexture("./Assets/Planets/tex1.jpg")
        self.Planet1.setTexture(tex, 1)

        self.Planet2 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet2.reparentTo(self.render)
        self.Planet2.setPos(2500, 4000, 2)
        self.Planet2.setHpr(132, 102, 142)
        self.Planet2.setScale(100)
        tex = self.loader.loadTexture("./Assets/Planets/tex2.jpg")
        self.Planet2.setTexture(tex, 1)

        self.Planet3 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet3.reparentTo(self.render)
        self.Planet3.setPos(-1600, 3200, -30)
        self.Planet3.setHpr(4, 63, 124)
        self.Planet3.setScale(100)
        tex = self.loader.loadTexture("./Assets/Planets/tex3.jpg")
        self.Planet3.setTexture(tex, 1)
        
        self.Planet4 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet4.reparentTo(self.render)
        self.Planet4.setPos(630, -4100, -3000)
        self.Planet4.setHpr(46, 31, 115)
        self.Planet4.setScale(200)
        tex = self.loader.loadTexture("./Assets/Planets/tex4.jpg")
        self.Planet4.setTexture(tex, 1)
        
        self.Planet5 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet5.reparentTo(self.render)
        self.Planet5.setPos(937, -8531, 5650)
        self.Planet5.setHpr(60, 36, 85)
        self.Planet5.setScale(250)
        tex = self.loader.loadTexture("./Assets/Planets/tex5.jpg")
        self.Planet5.setTexture(tex, 1)
        
        self.Planet6 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet6.reparentTo(self.render)
        self.Planet6.setPos(150, 5000, 67)
        self.Planet6.setHpr(136, 61, 4)
        self.Planet6.setScale(300)
        tex = self.loader.loadTexture("./Assets/Planets/tex6.jpg")
        self.Planet6.setTexture(tex, 1)
        
        self.Planet7 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet7.reparentTo(self.render)
        self.Planet7.setPos(1750, -1200, -1500)
        self.Planet7.setHpr(155, 27, 76)
        self.Planet7.setScale(350)
        tex = self.loader.loadTexture("./Assets/Planets/tex7.jpg")
        self.Planet7.setTexture(tex, 1)

        self.Dumbledore = self.loader.loadModel("./Assets/Spaceships/Dumbledore/Dumbledore.egg")
        self.Dumbledore.reparentTo(self.render)
        self.Dumbledore.setScale(2)
        tex = self.loader.loadTexture("./Assets/Spaceships/Dumbledore/spacejet_C.png")
        self.Dumbledore.setTexture(tex, 2)

        self.Station = self.loader.loadModel("./Assets/SpaceStation/SpaceStation1B/spaceStation.egg")
        self.Station.reparentTo(self.render)
        self.Station.setPos(353, 375, 208)
        self.Station.setHpr(102, 29, 18)
        self.Station.setScale(5)
        tex = self.loader.loadTexture("./Assets/SpaceStation/SpaceStation1B/SpaceStation1_Dif2.png")
        self.Station.setTexture(tex, 1)



app = MyApp()
app.run()