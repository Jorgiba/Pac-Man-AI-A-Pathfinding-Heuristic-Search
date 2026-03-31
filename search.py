# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).

Name student 1: Jorge Ibarreta
Name student 2: Sergio Rocha
IA lab group and pair: 1322 - 06

"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(search_problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions

    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(search_problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    print("Start:", search_problem.getStartState())
    print("Is the start a goal?",search_problem.isGoalState(search_problem.getStartState()))
    print("Start's successors:",search_problem.getSuccessors(search_problem.getStartState()))
    """

    # structure = util.Stack()
    # structure.push((search_problem.getStartState(), []))  # DEFINE THE INITIAL STATE
    # visited = []

    # while not structure.isEmpty():

    #     path = structure.pop()
    #     current_state = path[0]  # INDEX THE CURRENT STATE

    #     if search_problem.isGoalState(current_state):
    #         return path[1]  # RETURN THE PATH OF STATES

    #     if current_state not in visited:
    #         visited.append(current_state)

    #         for successor in search_problem.getSuccessors(current_state):
    #             if successor[0] not in visited:
    #                 new_path = (successor[0], path[1] + [successor[1]])  # CREATE THE NEW PATH OF STATES
    #                 structure.push(new_path)

    # return None
    counter = [0]
    def dfs_priority_func(e):
        state, path = e
        counter[0] -= 1
        return counter[0]
    
    return genericSearch(search_problem, util.PriorityQueueWithFunction(dfs_priority_func))

    

def genericSearch(search_problem, structure):
    structure.push((search_problem.getStartState(), []))
    visited = []

    while not structure.isEmpty():

        path = structure.pop()
        current_state = path[0]  # INDEX THE CURRENT STATE

        if search_problem.isGoalState(current_state):
            return path[1]  # RETURN THE PATH OF STATES

        if current_state not in visited:
            visited.append(current_state)

            for successor in search_problem.getSuccessors(current_state):
                if  successor[0] not in visited:
                    new_path = (successor[0], path[1] + [successor[1]])
                    structure.push(new_path)
                # if successor[0] not in visited:
                #     new_path = (successor[0], path[1] + [successor[1]])  # CREATE THE NEW PATH OF STATES
                #     if strategy == util.PriorityQueue and heuristic != None:
                #         structure.push(new_path, search_problem.getCostOfActions(path[1]) + successor[2] + heuristic(successor[0], search_problem)) 
                #     elif strategy == util.PriorityQueue and heuristic == None:
                #         structure.push(new_path, search_problem.getCostOfActions(path[1]) + successor[2])
                #     else:
                #         structure.push(new_path)

    return None



def breadthFirstSearch(search_problem):
    """
    Search the shallowest nodes in the search tree first.
    
    print("Start:", search_problem.getStartState())
    print("Is the start a goal?", search_problem.isGoalState(search_problem.getStartState()))
    print("Start's successors:", search_problem.getSuccessors(search_problem.getStartState()))
    """
    def bfs_priority_func(e):
        state, path = e
        return len(path)
    
    return genericSearch(search_problem, util.PriorityQueueWithFunction(bfs_priority_func))
    # structure = util.Queue()
    # structure.push((search_problem.getStartState(), []))
    # visited = []

    # while not structure.isEmpty():

    #     path = structure.pop()
    #     current_state = path[0]

    #     if search_problem.isGoalState(current_state):
    #         return path[1]

    #     if current_state not in visited:
    #         visited.append(current_state)

    #         for successor in search_problem.getSuccessors(current_state):
    #             if successor[0] not in visited:
    #                 new_path = (successor[0], path[1] + [successor[1]])
    #                 structure.push(new_path) 

    # return None 



def uniformCostSearch(search_problem):
    """Search the node of least total cost first."""
    def ucs_priority_func(e):
        state, path = e
        return search_problem.getCostOfActions(path)
    return genericSearch(search_problem, util.PriorityQueueWithFunction(ucs_priority_func))
    # structure = util.PriorityQueue()
    # structure.push((search_problem.getStartState(), []), 1)
    # visited = []

    # while not structure.isEmpty():

    #     path = structure.pop()
    #     current_state = path[0]

    #     if search_problem.isGoalState(current_state):
    #         return path[1]

    #     if current_state not in visited:
    #         visited.append(current_state)

    #         for successor in search_problem.getSuccessors(current_state):
    #             if successor[0] not in visited:
    #                 new_path = (successor[0], path[1] + [successor[1]])
    #                 structure.push(new_path, search_problem.getCostOfActions(path[1]) + successor[2]) 

    # return None 

def nullHeuristic(state, search_problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(search_problem, heuristic=nullHeuristic):

    def astar_priority_func(e):
        state, path = e
        return search_problem.getCostOfActions(path) + heuristic(state, search_problem)
    
    return genericSearch(search_problem, util.PriorityQueueWithFunction(astar_priority_func))

    # """Search the node that has the lowest combined cost and heuristic first."""
    # structure = util.PriorityQueue()
    # structure.push((search_problem.getStartState(), []), 1)
    # visited = []

    # while not structure.isEmpty():

    #     path = structure.pop()
    #     current_state = path[0]

    #     if search_problem.isGoalState(current_state):
    #         return path[1]

    #     if current_state not in visited:
    #         visited.append(current_state)

    #         for successor in search_problem.getSuccessors(current_state):
    #             if successor[0] not in visited:
    #                 new_path = (successor[0], path[1] + [successor[1]])
    #                 structure.push(new_path, search_problem.getCostOfActions(path[1]) + successor[2] + heuristic(successor[0], search_problem)) 

    # return None 




# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch