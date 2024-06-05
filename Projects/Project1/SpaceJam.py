from direct.showbase.ShowBase import ShowBase

class MyApp(ShowBase):

    def __init__(self):
        
        ShowBase.__init__(self)
        self.SetupScene()

    def SetupScene(self):

        self.Universe = self.loader.loadModel("./Assets/Universe/Universe.x")
        self.Universe.reparentTo(self.render)
        self.Universe.setScale(15000)
        tex = self.loader.loadTexture("./Assets/Universe/starfield-in-blue.jpg")
        self.Universe.setTexture(tex, 1)

        self.Planet1 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet1.reparentTo(self.render)
        self.Planet1.setPos(150, 5000, 67)
        self.Planet1.setScale(350)
        tex = self.loader.loadTexture("./Assets/Planets/mh_gas__22.jpg")
        self.Planet1.setTexture(tex, 1)



app = MyApp()
app.run()