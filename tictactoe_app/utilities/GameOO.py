class GameOO:
    def __init__(self, pk, board, playerTurn=1):
        self.pk = pk
        self.board = 9*[''] if None else board
        self.playerTurn=playerTurn
    

    def validMove(self, square):
        if(square>=0 and square<9):
            return (self.board[square]=='')
        else:
            return False
        
        
    def makeMove(self, square):
        if(self.validMove(square)):
            if(self.playerTurn==1):
                self.board[square]='X'
            else:
                self.board[square]='O'
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
        if(self.board[0]==symbol):
            if(self.board[1]==symbol and self.board[2]==symbol
                or self.board[4]==symbol and self.board[8]==symbol):
                return self.playerTurn+' wins!'
        elif(self.board[1]==symbol and self.board[4]==symbol and self.board[7]==symbol):
            return self.playerTurn+' wins!'
        elif(self.board[2]==symbol and self.board[5]==symbol and self.board[8]==symbol):
            return self.playerTurn+' wins!'
        elif(self.board[3]==symbol and self.board[4]==symbol and self.board[5]==symbol):
            return self.playerTurn+' wins!'
        elif(self.board[6]==symbol):
            if(self.board[7]==symbol and self.board[8]==symbol
                or self.board[4]==symbol and self.board[2]==symbol):
                return self.playerTurn+' wins!'
        elif('' not in self.board):
            return 'Tie game!'
        else:
            return 'Not over'

