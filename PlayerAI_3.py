from random import randint
from BaseAI_3 import BaseAI
import time
import math


class PlayerAI(BaseAI):

    def __init__(self):
        self.points = [[6,5,4,3],[5,4,3,2],[4,3,2,1],[3,2,1,0]]
        self.time = 0.0
        
    def getMove(self, grid):
        max_move = None
        self.time = time.clock()
        moves = grid.getAvailableMoves()
        cell = len(grid.getAvailableCells())
        if cell <= 4:
            depth = 6
        elif cell <= 8:
            depth = 4
        else:
            depth = 2
        
        if len(moves)!= 0:
            max_alpha = float('-inf')
            min_beta = float('inf')
            
            for move in moves:
                gridCopy = grid.clone()
                
                if gridCopy.canMove([move]):
                    gridCopy.move(move)
                    alpha = self.minimize(gridCopy, max_alpha, min_beta, depth)
                     
                    if alpha > max_alpha:        
                        max_alpha = alpha
                        max_move = move
                            
        return max_move    


    def terminate(self, grid, depth ):
        state = False
        
        if depth < 0:
            state = True
            
        elif len(grid.getAvailableMoves()) == 0 or len(grid.getAvailableCells())==0:
            state = True
            
        return state

    def maximize(self, grid, alpha, beta, depth):
 
        if self.terminate(grid, depth):
            score = self.heruistic(grid)
            return score
        
        moves = grid.getAvailableMoves()
        alpha = float("-inf")
        
        for move in moves:
            gridCopy = grid.clone()
            if gridCopy.canMove([move]):
                gridCopy.move(move)
                score = self.minimize(gridCopy, alpha, beta, depth-1)
                if score > alpha:
                    alpha = score
                if beta <= alpha:
                    break
        return alpha
                



     

















        
        

    
