import Board

class Engine:

    p1name = ""
    p2name = ""
    p1var = ""
    p2var = ""
    x_coordinate = ""
    y_coordinate = ""
    chance = 0
    end = False
    tie = False

    def __init__(self):
        Engine.startGame()
        self.p1name = Engine.p1name
        self.p2name = Engine.p2name
        self.p1var = Engine.p1var
        self.p2var = Engine.p2var

        Board.Board().showBoard()
        while Engine.tie == False:
            for i in range(0, 3):
                for j in range(0, 3):
                    if Board.Board.b00 == Board.Board.b01 and Board.Board.b00 == Board.Board.b02 and Board.Board.b00 != "" and Board.Board.b01 != 0 and Board.Board.b02 != 0:
                        if Board.Board.b00 == "X":
                            print(f"{Engine.p1name} WON!")
                            quit()
                        else:
                            print(f"{Engine.p2name} WON!")
                            quit()
                    elif Board.Board.b10 == Board.Board.b11 and Board.Board.b10 == Board.Board.b12 and Board.Board.b10 != "" and Board.Board.b11 != 0 and Board.Board.b12 != 0:
                        if Board.Board.b10 == "X":
                            print(f"{Engine.p1name} WON!")
                            quit()
                        else:
                            print(f"{Engine.p2name} WON!")
                            quit()
                    elif Board.Board.b20 == Board.Board.b21 and Board.Board.b20 == Board.Board.b22 and Board.Board.b20 != "" and Board.Board.b21 != 0 and Board.Board.b22 != 0:
                        if Board.Board.b20 == "X":
                            print(f"{Engine.p1name} WON!")
                            quit()
                        else:
                            print(f"{Engine.p2name} WON!")
                            quit()
                    elif Board.Board.b00 == Board.Board.b11 and Board.Board.b00 == Board.Board.b22 and Board.Board.b00 != "" and Board.Board.b11 != 0 and Board.Board.b22 != 0:
                        if Board.Board.b00 == "X":
                            print(f"{Engine.p1name} WON!")
                            quit()
                        else:
                            print(f"{Engine.p2name} WON!")
                            quit()
                    elif Board.Board.b02 == Board.Board.b11 and Board.Board.b02 == Board.Board.b20 and Board.Board.b02 != "" and Board.Board.b11 != 0 and Board.Board.b20 != 0:
                        if Board.Board.b02 == "X":
                            print(f"{Engine.p1name} WON!")
                            quit()
                        else:
                            print(f"{Engine.p2name} WON!")
                            quit()
                    elif Board.Board.b00 == Board.Board.b10 and Board.Board.b00 == Board.Board.b20 and Board.Board.b00 != "" and Board.Board.b10 != 0 and Board.Board.b20 != 0:
                        if Board.Board.b00 == "X":
                            print(f"{Engine.p1name} WON!")
                            quit()
                        else:
                            print(f"{Engine.p2name} WON!")
                            quit()
                    elif Board.Board.b01 == Board.Board.b11 and Board.Board.b01 == Board.Board.b21 and Board.Board.b01 != "" and Board.Board.b11 != 0 and Board.Board.b21 != 0:
                        if Board.Board.b01 == "X":
                            print(f"{Engine.p1name} WON!")
                            quit()
                        else:
                            print(f"{Engine.p2name} WON!")
                            quit()  
                    elif Board.Board.b02 == Board.Board.b12 and Board.Board.b02 == Board.Board.b22 and Board.Board.b02 != "" and Board.Board.b12 != 0 and Board.Board.b22 != 0:
                        if Board.Board.b02 == "X":
                            print(f"{Engine.p1name} WON!")
                            quit()
                        else:
                            print(f"{Engine.p2name} WON!")
                            quit()
            if Board.Board.b00 != "" and Board.Board.b01 != "" and Board.Board.b02 != "" and Board.Board.b10 != "" and Board.Board.b11 != "" and Board.Board.b12 != "" and Board.Board.b20 != "" and Board.Board.b21 != "" and Board.Board.b22 != "":
                print("TIE!")
                Engine.tie = True
                quit()
            if Engine.chance == 0:
                print(f"{self.p1name}'s TURN")
                Engine.getXCoordinate()
                Engine.getYCoordinate()
                
                if Engine.x_coordinate == 0 and Engine.y_coordinate == 0 and Board.Board.b00 == "":
                    Board.Board.b00 = Engine.p1var
                    Board.Board().showBoard()
                    Engine.chance = 1
                elif Engine.x_coordinate == 0 and Engine.y_coordinate == 1 and Board.Board.b01 == "":
                    Board.Board.b01 = Engine.p1var
                    Board.Board().showBoard()
                    Engine.chance = 1
                elif Engine.x_coordinate == 0 and Engine.y_coordinate == 2 and Board.Board.b02 == "":
                    Board.Board.b02 = Engine.p1var
                    Board.Board().showBoard()
                    Engine.chance = 1
                elif Engine.x_coordinate == 1 and Engine.y_coordinate == 0 and Board.Board.b10 == "":
                    Board.Board.b10 = Engine.p1var
                    Board.Board().showBoard()
                    Engine.chance = 1
                elif Engine.x_coordinate == 1 and Engine.y_coordinate == 1 and Board.Board.b11 == "":
                    Board.Board.b11 = Engine.p1var
                    Board.Board().showBoard()
                    Engine.chance = 1
                elif Engine.x_coordinate == 1 and Engine.y_coordinate == 2 and Board.Board.b12 == "":
                    Board.Board.b12 = Engine.p1var
                    Board.Board().showBoard()
                    Engine.chance = 1
                elif Engine.x_coordinate == 2 and Engine.y_coordinate == 0 and Board.Board.b20 == "":
                    Board.Board.b20 = Engine.p1var
                    Board.Board().showBoard()
                    Engine.chance = 1
                elif Engine.x_coordinate == 2 and Engine.y_coordinate == 1 and Board.Board.b21 == "":
                    Board.Board.b21 = Engine.p1var
                    Board.Board().showBoard()
                    Engine.chance = 1
                elif Engine.x_coordinate == 2 and Engine.y_coordinate == 2 and Board.Board.b22 == "":
                    Board.Board.b22 = Engine.p1var
                    Board.Board().showBoard()
                    Engine.chance = 1
                else:
                    print("COORDINATES ALREADY IN USE!")

            else:
                print(f"{self.p2name}'s TURN")
                Engine.getXCoordinate()
                Engine.getYCoordinate()
                if Engine.x_coordinate == 0 and Engine.y_coordinate == 0 and Board.Board.b00 == "":
                    Board.Board.b00 = Engine.p2var
                    Board.Board().showBoard()
                    Engine.chance = 0
                elif Engine.x_coordinate == 0 and Engine.y_coordinate == 1 and Board.Board.b01 == "":
                    Board.Board.b01 = Engine.p2var
                    Board.Board().showBoard()
                    Engine.chance = 0
                elif Engine.x_coordinate == 0 and Engine.y_coordinate == 2 and Board.Board.b02 == "":
                    Board.Board.b02 = Engine.p2var
                    Board.Board().showBoard()
                    Engine.chance = 0
                elif Engine.x_coordinate == 1 and Engine.y_coordinate == 0 and Board.Board.b10 == "":
                    Board.Board.b10 = Engine.p2var
                    Board.Board().showBoard()
                    Engine.chance = 0
                elif Engine.x_coordinate == 1 and Engine.y_coordinate == 1 and Board.Board.b11 == "":
                    Board.Board.b11 = Engine.p2var
                    Board.Board().showBoard()
                    Engine.chance = 0
                elif Engine.x_coordinate == 1 and Engine.y_coordinate == 2 and Board.Board.b12 == "":
                    Board.Board.b12 = Engine.p2var
                    Board.Board().showBoard()
                    Engine.chance = 0
                elif Engine.x_coordinate == 2 and Engine.y_coordinate == 0 and Board.Board.b20 == "":
                    Board.Board.b20 = Engine.p2var
                    Board.Board().showBoard()
                    Engine.chance = 0
                elif Engine.x_coordinate == 2 and Engine.y_coordinate == 1 and Board.Board.b21 == "":
                    Board.Board.b21 = Engine.p2var
                    Board.Board().showBoard()
                    Engine.chance = 0
                elif Engine.x_coordinate == 2 and Engine.y_coordinate == 2 and Board.Board.b22 == "":
                    Board.Board.b22 = Engine.p2var
                    Board.Board().showBoard()
                    Engine.chance = 0
                else:
                    print("COORDINATES ALREADY IN USE!")
    @classmethod
    def startGame(cls):
        print('WELCOME TO TIC TAC TOE!')
        cls.p1name = input("ENTER PLAYER 1 NAME:- ")
        cls.p2name = input("ENTER PLAYER 2 NAME:- ")
        cls.p1var = "X"
        cls.p2var = "0"
        print(f"{cls.p1name}'s variable is {cls.p1var} and {cls.p2name}'s variable is {cls.p2var}")

    @classmethod
    def getXCoordinate(cls):
        cls.x_coordinate = int(input("ENTER X COORDINATE:- "))
    @classmethod
    def getYCoordinate(cls):
        cls.y_coordinate = int(input("ENTER Y COORDINATE:- "))

if __name__ == "__main__":
    Engine()