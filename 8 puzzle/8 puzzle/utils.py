# -*- coding: utf-8 -*-



def goalPrint(state,expanded):
    search_depth = 0
    goal_states = []
    
    cost = state.cost
    
    while state.parent != None:
        search_depth += 1
        goal_states.append(state)
        state = state.parent
    goal_states.reverse()
    
    print('path_to_goal: ',[g.action for g in goal_states])
    print("cost_of_path: ", cost)
    print('nodes_expanded: ', expanded)
    print('search_depth: ', search_depth)