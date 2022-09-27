class environment:
    # 2D Grid environment init and defaults
    xSize = 0
    ySize = 0
    zSize = 0
    grid = []
    row = []
    emptyCell = "| |" 

    # Standard environment init
    def __init__(self, x_In, y_In) -> None:
        self.xSize = x_In
        self.ySize = y_In
        for i in range(self.ySize):
            for j in range (self.xSize):
                self.grid.append(self.emptyCell)
            self.grid.append("\n")
        print(self.grid)


    # Overloaded init for 3D environment with z-dimension
    # def __init__(self, x_In, y_In, z_In) -> None:
    #     self.xSize = x_In
    #     self.ySize = y_In
    #     self.zSize = z_In

    def displayEnviron():
        for i in range(environment.ySize):
            for j in range (environment.xSize):
                print(environment.grid)    

