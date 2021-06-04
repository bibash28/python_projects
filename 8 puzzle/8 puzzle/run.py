# -*- coding: utf-8 -*-

from eightpuzzle import PuzzleState
from utils import goalPrint
import math

import queue as Q
import time



def bfs_search(initial_state,goal_state):

    """BFS search"""
    time1 = time.time()
    max_search_depth = 0
    expanded = -1
    frontier = Q.Queue()
    frontierDict = {}
    
    frontier.put(initial_state)
    while not frontier.empty() :
        #REMOVE
        state = frontier.get()
        frontierDict[state.config] = state
        state.expand()

        expanded += 1
        
        #GOAL CHECK
        if state.config == goal_state.config:
        
            goalPrint(state,expanded)
            print('max_search_depth: ',max_search_depth)
            print('running_time: ', time.time()-time1)
            
            return state
          
        state_neighbours = [state.move_up(),state.move_down(),state.move_left(),state.move_right()]
        state_neighbours =  [x for x in state_neighbours if x is not None]
#        state_neighbours.reverse()
        #EXPAND
        for i in state_neighbours:            
            if i.config not in frontierDict:             
                # these are the node in the queue, not the expanded nodes sucker
                frontier.put(i)
                frontierDict[i.config] = i

            if i.cost >= max_search_depth :
                    max_search_depth = i.cost
              

def main():

    begin_state = (0,8,7,6,5,4,3,2,1)
    #  1,2,5,3,4,0,6,7,8
    size = int(math.sqrt(len(begin_state)))
    
    goal_state = PuzzleState((0,1,2,3,4,5,6,7,8),size)
    hard_state = PuzzleState(begin_state, size)
    
    bfs_search(hard_state,goal_state)  
    
if __name__ == '__main__':
    main()

    
    
    
    