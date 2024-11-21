class GameOO:
    def __init__(self, board=None, playerTurn=1):
        self.board = 9*[''] if board is None else board
        self.playerTurn=playerTurn
        self.winner=None
    
    def printBoard(self):
        print(self.board[0:3])
        print(self.board[3:6])
        print(self.board[6:9])


    def validMove(self, square):
        if(self.winner is None):
            try:
                square=int(square)
                if(square>=0 and square<9):
                    return (self.board[square]=='')
                else:
                    return False
            except TypeError:
                return False
            except ValueError:
                return False
        else:
            return False
        
        
    def makeMove(self, square):
        if(self.validMove(square)):
            if(self.playerTurn==1):
                self.board[square]='X'
            else:
                self.board[square]='O'
            self.checkGameOver()
        else:
            pass 
    

    def checkGameOver(self):
        # someone won, tie game, or not over?
        # if the player got 3 of their symbol then they win
        # else if all squares are full then it's a tie
        symbol=''
        if(self.playerTurn==1):
            symbol='X'
        elif(self.playerTurn==2):
            symbol='O'
        else:
            return ValueError
        if(self.board[0]==symbol and self.board[1]==symbol and self.board[2]==symbol):
            self.winner=self.playerTurn
        elif(self.board[0]==symbol and self.board[4]==symbol and self.board[8]==symbol):
            self.winner=self.playerTurn
        elif(self.board[1]==symbol and self.board[4]==symbol and self.board[7]==symbol):
            self.winner=self.playerTurn
        elif(self.board[2]==symbol and self.board[5]==symbol and self.board[8]==symbol):
            self.winner=self.playerTurn
        elif(self.board[3]==symbol and self.board[4]==symbol and self.board[5]==symbol):
            self.winner=self.playerTurn
        elif(self.board[6]==symbol and self.board[7]==symbol and self.board[8]==symbol):
            self.winner=self.playerTurn
        elif(self.board[6]==symbol and self.board[4]==symbol and self.board[2]==symbol):
            self.winner=self.playerTurn
        elif('' not in self.board):
            self.winner=3
        else:
            # 'Not over'
            if(self.playerTurn==1):
                self.playerTurn=2
            else:
                self.playerTurn=1

def tester():
    Game = GameOO()
    while(Game.winner is None):
        Game.printBoard()
        print(f"Player {Game.playerTurn} turn.")
        square=-1
        while(not Game.validMove(square)):
            square=input("Enter square")
        square=int(square)
        Game.makeMove(square)
    Game.printBoard()
    if(Game.winner==1):
        print("player 1 wins")
    elif(Game.winner==2):
        print("player 2 wins")
    elif(Game.winner==3):
        print("Game is a tie")
    else:
        print("You broke the game")