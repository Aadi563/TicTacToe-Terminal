class Board:
    b00 = ""
    b01 = ""
    b02 = ""
    b10 = ""
    b11 = ""
    b12 = ""
    b20 = ""
    b21 = ""
    b22 = ""

    def showBoard(self):
        print()
        print(f"| |\t{Board.b00}\t|", f"|\t{Board.b01}\t|", f"|\t{Board.b02}\t| |")
        print("_"*17, "_"*15, "_"*17)
        print()
        print(f"| |\t{Board.b10}\t|", f"|\t{Board.b11}\t|", f"|\t{Board.b12}\t| |")
        print("_"*17, "_"*15, "_"*17)
        print()
        print(f"| |\t{Board.b20}\t|", f"|\t{Board.b21}\t|", f"|\t{Board.b22}\t| |")
        print()

if __name__ == "__main__":
    pass        