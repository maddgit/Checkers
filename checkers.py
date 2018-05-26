
"""

 USER DISPLAY--------------
     . y . y . y . y
     y . y . y . y .
     . y . y . y . y
     . . . . . . . .
     . . . . . . . .
     x . x . x . x .
     . x . x . x . x
     x . x . x . x .

 NUMBERED LOCATIONS--------
     0  1  2  3  4  5  6  7  
     8  9 10 11 12 13 14 15
    16 17 18 19 20 21 22 23
    24 25 26 27 28 29 30 31
    32 33 34 35 36 37 38 39
    40 41 42 43 44 45 46 47
    48 49 50 51 52 53 54 55
    56 57 58 59 60 61 62 63    

"""

import random

board = ['.','y','.','y','.','y','.','y',
        'y','.','y','.','y','.','y','.',
        '.','y','.','y','.','y','.','y',
        '.','.','.','.','.','.','.','.',
        '.','.','.','.','.','.','.','.',
        'x','.','x','.','x','.','x','.',
        '.','x','.','x','.','x','.','x',
        'x','.','x','.','x','.','x','.']

class Board():
    def __init__(self, board):
        self.board = board

    def prettyPrint(self):
        print "      "
        print "\n".join([" ".join(self.board[i : i + 8]) for i in xrange(0,len(self.board), 8)])
        print " "
                
    def updateBoard(self, s1, s2): # not associated w private variable
        self.board[s2]= self.board[s1]
        self.board[s1]= '.'
        return (self.prettyPrint())

    def GameOver(self, players): #current_player, ie: 'x' or 'y' not in list 
        if players[0] == 'x':
            if 'x' or 'X' in self.board:
                return False
            else:
                print "X's Lose. Better Luck Next Time "
        elif players[0] == 'y':
            if 'y' or 'Y' in self.board:
                return False
            else:
                print "Y's Lose. Better Luck Next Time "

    def capture(self, s1, s2):                           
        self.board[((s2-s1)/2)+ s1] = '.'

    def make_king(self, s1, s2, players):
        if players[0] == 'x':
            self.board[s1] = 'X'
        else:
            self.board[s1] = 'Y'
              
    def isKingsRow(self, s2, players):
        if players[0]== 'x' and s2 in (1, 3, 5, 7): # KingsRow index for x 
            return True
        elif players[0] == 'y' and s2 in (56, 58, 60, 62): # KingsRow index for y
            return True
        else:
            return False

    def hop_move(self, s1, s2):
        if s2 - s1 in (14, 18, -14, -18,):
            return True
        else:
            return False

    def valid_hop(self, s1, s2):
        if (self.hop_move(s1, s2)):
            s3 = ((s2-s1)/2) + s1
            if (self.board[s3] == self.board[s1]) or (self.board[s3]) == '.': #only if opponant piece
                print "Try again. You must only hop over an opponant's piece."
            else:
                return True
        else:
            return False

    def adj_move(self, s1, s2):
        if s2 - s1 in (7, 9, -7, -9,):
            return True
        else:
            return False
            
    def isKings(self, s1):
        if self.board[s1] in ('Y','X'):
            return True
        else:
            return False

    def backwards(self, s1, s2, players):
        if (players[0] == 'x' and s2 - s1 > 0) or (players[0]== 'y' and s2 - s1 < 0):
            return True
        else:
            return False

    def diagonol(self, s1, s2):
        if s2 - s1 in (7, 9, 14, 18, -7, -9, -14, -18):
            return True
        else:
            print "Try again. You must move to a diagonol position."
              
    def real_pos(self, s1, s2):
        if 0 <= s1 <= 63 and 0 <= s2 <= 63:
            return True
        else:
            print "You must move to a legal position on the board"
              
    def not_taken(self):
        if self.board[s2] == '.':
            return True
        else:
            print "You must move to an empty space."
              
    def right_turn(self, players):
        if (players[0]== 'x' and self.board[s1] in ('x','X')) or (players[0]== 'y' and self.board[s1] in ('y','Y')):
            return True
        else:
            print "Only move pieces that belong to you and are between 0-63."
            
    def compfalse(self, s1, s2):
        if s1 == -13 and s2 == -9:
            return True
        else:
            return False
          
    def is_valid(self, s1, s2, players):
        if (self.compfalse(s1, s2)):
            return False
        else:
            if (self.right_turn(players)) and (self.real_pos(s1, s2)):
                if (self.not_taken()) and (self.diagonol(s1, s2)):
                    if ((self.backwards(s1, s2, players)) and (self.isKings(s1))) or (not(self.backwards(s1, s2, players)) and not(self.isKings(s1))):
                        if (self.valid_hop(s1, s2)) or (self.adj_move(s1, s2)):
                            return True
                        else:
                            return False
                    else:
                        print "Only Kings can move backwards."
                else:
                    return False
            else:
                return False

    def get_change(self, s1, s2, players):
        if (self.valid_hop(s1, s2)):
            if (self.isKingsRow(s2, players)):
                if not (self.isKings(s1)):
                    (self.make_king(s1, s2, players))(self.capture(s1, s2))
                else:
                    (self.capture(s1, s2))
            else:
                (self.capture(s1, s2))
        else:
            if (self.isKingsRow(s2, players)):
                if not(self.isKings(s1)):
                    (self.make_king(s1, s2, players))
                else:
                    pass
            else:
                pass
                  
b = Board(board)

intro = """
------------WELCOME-TO---------------------------
                        CHECKERS  
 Numbered Locations - ------------ - Board
  0  1  2  3  4  5  6  7   . y . y . y . y
  8  9 10 11 12 13 14 15   y . y . y . y .
 16 17 18 19 20 21 22 23   . y . y . y . y
 24 25 26 27 28 29 30 31   . . . . . . . .
 32 33 34 35 36 37 38 39   . . . . . . . .
 40 41 42 43 44 45 46 47   x . x . x . x .
 48 49 50 51 52 53 54 55   . x . x . x . x
 56 57 58 59 60 61 62 63   x . x . x . x .
   """

print intro

guide ="""                [  1   3   5   7
                  8  10  12  14  ]
                [  17  19  21  23
                 24  26  28  30  ]
                [  33  35  37  39
                 40  42  44  46  ]
                [  49  51  53  55
                 56 _58 _60 _62 _|         
"""



game_type = ''
game_type = raw_input("   Please Type 'D' for Double Player Mode, or 'S'\n   for Single Player Mode: ")
                                                                 

s1 = -13
s2 = -9

players = ['x','y']
current_player = players[0]
                     
if game_type == 'D':
    print "   Double Player Mode: Human v Human. X's Go First."
    while b.GameOver(players) == False:
        print guide
        s1 = inp = input("   Type # location of piece you want to move: ")
        s2 = inp = input("   Type # location of intended destination: ")
        if (b.is_valid(s1, s2, players)):
            (b.get_change(s1, s2, players)) 
            (b.updateBoard(s1, s2))
            players = players[::-1]
        else:
            pass
    print "Restart to Play Again."

if game_type == 'S':
    print "   Single Player Mode: Human v Program. X's (human) Goes First."
    while b.GameOver(players) == False:
        while players[0] == 'x':
            print guide
            s1 = inp = input("   Type # location of piece you want to move: ")
            s2 = inp = input("   Type # location of intended destination: ")
            if (b.is_valid(s1, s2, players)):
                (b.get_change(s1, s2, players)) 
                (b.updateBoard(s1, s2))
                players = players[::-1]
            else:
                pass


        print  "   The Program Made its Move. Your Turn Again, X's...    "
        pieces = [index for index, letter in enumerate(board) if letter in ('y', 'Y')]

        left_hop =[]
        for n in pieces:
            if board[n+9] =='x' and board[n+18] =='.'and n not in (7, 23, 39, 47, 63):
                left_hop.append(n)

        right_hop =[]
        for n in pieces:
            if board[n+7] =='x' and board[n+14] =='.' and n not in (8, 24, 40, 56):
                right_hop.append(n)

        hoplist = right_hop + left_hop
        
#-------------------------------------
        left_adj=[]
        for n in pieces:
            if board[n+9] =='.' and board[n+18] =='.' and n not in (7, 23, 39, 47, 63):
                left_adj.append(n)

        right_adj=[]
        for n in pieces:
            if board[n+7] =='.' and board[n+14] =='.' and n not in (8, 24, 40, 56):
                right_adj.append(n)

        adj_safe = right_adj + left_adj
        
#--------------------------------------
        worst_left=[]
        for n in pieces: 
            if board[n+9] =='.' and board[n+18] =='x' and n not in (7, 23, 39, 47, 63):
                worst_left.append(n)

        worst_right=[]
        for n in pieces:
            if board[n+7] =='.' and board[n+14] =='x' and n not in (8, 24, 40, 56):
                worst_right.append(n)

        worst_move = worst_right + worst_left
        
#-------------------Getting s1-----------------
        if len(left_hop) > 0 or len(right_hop) > 0:
            s1 = (random.choice(hoplist))
        elif len(left_adj) > 0 or len(right_adj) > 0:
            s1 = (random.choice(adj_safe))
        else:
            s1 = (random.choice(worst_move))
            
#-------------------Getting s2-------------
        if s1 in hoplist:
            if s1 in left_hop:
                s2 = s1 + 18
            else:
                s2 = s1 +14
        elif s1 in adj_safe:
            if s1 in left_adj:
                s2 = s1 + 9
            else:
                s2 = s1 + 7
        elif s1 in worst_move:
            if s1 in worst_left:
                s2 = s1 + 9
            else:
                s2 = s1 + 7
                
#--Retrieved and now pop back into Board class methods-
        (b.get_change(s1, s2, players)) 
        (b.updateBoard(s1, s2))
        players = players[::-1] # switch back to player x
        
    print "Restart to PLay Again"



    
