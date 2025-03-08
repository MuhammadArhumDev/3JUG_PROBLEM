# Copyright (c) 2025 Muhammad Arhum  
# All rights reserved. 

# Unauthorized copying, modification, or distribution of this code,  
# via any medium, is strictly prohibited without prior permission. 

# MuhammadArhum - 2025-03-08  
# GitHub: @MuhammadArhumDev 
# LinkedIn: @MuhammadArhum 


from collections import deque
import heapq

def BFS_3JUG():
    capacities = (8, 5, 3)
    initialState = (8, 0, 0)
    goalState = (4, 4, 0)
    queue = deque([(initialState, [initialState])])
    visited = set([initialState])
    def getSuccessors(state):
        successors = []
        a, b, c = state
        def pour(state, i, j):
            stateList = list(state)
            if stateList[i] == 0 or stateList[j] == capacities[j]:
                return None
            amount = min(stateList[i], capacities[j] - stateList[j])
            stateList[i] -= amount
            stateList[j] += amount
            return tuple(stateList)
        moves = [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
        for i, j in moves:
            newState = pour(state, i, j)
            if newState is not None:
                successors.append(newState)
        return successors
    while queue:
        currentState, path = queue.popleft()
        if currentState == goalState:
            return path
        for nextState in getSuccessors(currentState):
            if nextState not in visited:
                visited.add(nextState)
                queue.append((nextState, path + [nextState]))
    return None

def DFS_3JUG():
    capacities = (8, 5, 3)
    initialState = (8, 0, 0)
    goalState = (4, 4, 0)
    stack = [(initialState, [initialState])]
    visited = set([initialState])
    def getSuccessors(state):
        successors = []
        a, b, c = state
        def pour(state, i, j):
            stateList = list(state)
            if stateList[i] == 0 or stateList[j] == capacities[j]:
                return None
            amount = min(stateList[i], capacities[j] - stateList[j])
            stateList[i] -= amount
            stateList[j] += amount
            return tuple(stateList)
        moves = [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
        for i, j in moves:
            newState = pour(state, i, j)
            if newState is not None:
                successors.append(newState)
        return successors
    while stack:
        currentState, path = stack.pop()
        if currentState == goalState:
            return path
        for nextState in getSuccessors(currentState):
            if nextState not in visited:
                visited.add(nextState)
                stack.append((nextState, path + [nextState]))
    return None

def IDS_3JUG():
    capacities = (8, 5, 3)
    initialState = (8, 0, 0)
    goalState = (4, 4, 0)
    def getSuccessors(state):
        successors = []
        a, b, c = state
        def pour(state, i, j):
            stateList = list(state)
            if stateList[i] == 0 or stateList[j] == capacities[j]:
                return None
            amount = min(stateList[i], capacities[j] - stateList[j])
            stateList[i] -= amount
            stateList[j] += amount
            return tuple(stateList)
        moves = [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
        for i, j in moves:
            newState = pour(state, i, j)
            if newState is not None:
                successors.append(newState)
        return successors
    def dfsLimited(state, path, depth):
        if state == goalState:
            return path
        if depth == 0:
            return None
        for nextState in getSuccessors(state):
            if nextState not in path:
                result = dfsLimited(nextState, path + [nextState], depth - 1)
                if result is not None:
                    return result
        return None
    depth = 0
    while True:
        result = dfsLimited(initialState, [initialState], depth)
        if result is not None:
            return result
        depth += 1

def UCS_3JUG():
    capacities = (8, 5, 3)
    initialState = (8, 0, 0)
    goalState = (4, 4, 0)
    frontier = []
    heapq.heappush(frontier, (0, initialState, [initialState]))
    visited = {initialState: 0}
    def getSuccessors(state):
        successors = []
        a, b, c = state
        def pour(state, i, j):
            stateList = list(state)
            if stateList[i] == 0 or stateList[j] == capacities[j]:
                return None
            amount = min(stateList[i], capacities[j] - stateList[j])
            stateList[i] -= amount
            stateList[j] += amount
            return tuple(stateList)
        moves = [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
        for i, j in moves:
            newState = pour(state, i, j)
            if newState is not None:
                successors.append(newState)
        return successors
    while frontier:
        cost, currentState, path = heapq.heappop(frontier)
        if currentState == goalState:
            return path
        for nextState in getSuccessors(currentState):
            newCost = cost + 1
            if nextState not in visited or newCost < visited[nextState]:
                visited[nextState] = newCost
                heapq.heappush(frontier, (newCost, nextState, path + [nextState]))
    return None

def GREEDY_3JUG():
    capacities = (8, 5, 3)
    initialState = (8, 0, 0)
    goalState = (4, 4, 0)
    def heuristic(state):
        return abs(state[0] - 4) + abs(state[1] - 4) + abs(state[2] - 0)
    frontier = []
    heapq.heappush(frontier, (heuristic(initialState), initialState, [initialState]))
    visited = set([initialState])
    def getSuccessors(state):
        successors = []
        a, b, c = state
        def pour(state, i, j):
            stateList = list(state)
            if stateList[i] == 0 or stateList[j] == capacities[j]:
                return None
            amount = min(stateList[i], capacities[j] - stateList[j])
            stateList[i] -= amount
            stateList[j] += amount
            return tuple(stateList)
        moves = [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
        for i, j in moves:
            newState = pour(state, i, j)
            if newState is not None:
                successors.append(newState)
        return successors
    while frontier:
        h, currentState, path = heapq.heappop(frontier)
        if currentState == goalState:
            return path
        for nextState in getSuccessors(currentState):
            if nextState not in visited:
                visited.add(nextState)
                heapq.heappush(frontier, (heuristic(nextState), nextState, path + [nextState]))
    return None

def A_STAR_3JUG():
    capacities = (8, 5, 3)
    initialState = (8, 0, 0)
    goalState = (4, 4, 0)
    def heuristic(state):
        return abs(state[0]-4) + abs(state[1]-4) + abs(state[2]-0)
    frontier = []
    heapq.heappush(frontier, (heuristic(initialState), 0, initialState, [initialState]))
    visited = {initialState: 0}
    def getSuccessors(state):
        successors = []
        a, b, c = state
        def pour(state, i, j):
            stateList = list(state)
            if stateList[i] == 0 or stateList[j] == capacities[j]:
                return None
            amount = min(stateList[i], capacities[j] - stateList[j])
            stateList[i] -= amount
            stateList[j] += amount
            return tuple(stateList)
        moves = [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
        for i, j in moves:
            newState = pour(state, i, j)
            if newState is not None:
                successors.append(newState)
        return successors
    while frontier:
        f, cost, currentState, path = heapq.heappop(frontier)
        if currentState == goalState:
            return path
        for nextState in getSuccessors(currentState):
            newCost = cost + 1
            if nextState not in visited or newCost < visited[nextState]:
                visited[nextState] = newCost
                newF = newCost + heuristic(nextState)
                heapq.heappush(frontier, (newF, newCost, nextState, path + [nextState]))
    return None

print("=== Linkedin@MuhammadArhum ===")
print("=== Github@MuhammadArhumDev - 2025-03-08 ===")
print("\n")

solutionBFS = BFS_3JUG()
if solutionBFS:
    print("=== BFS SOLUTION PATH ===")
    for i in range(len(solutionBFS) - 1):
        print(f"{solutionBFS[i]}  =>  {solutionBFS[i+1]}")
else:
    print("BFS: SOLUTION NOT POSSIBLE")

print("\n")

solutionDFS = DFS_3JUG()
if solutionDFS:
    print("=== DFS SOLUTION PATH ===")
    for i in range(len(solutionDFS) - 1):
        print(f"{solutionDFS[i]}  =>  {solutionDFS[i+1]}")
else:
    print("DFS: SOLUTION NOT POSSIBLE")

print("\n")

solutionIDS = IDS_3JUG()
if solutionIDS:
    print("=== IDS SOLUTION PATH ===")
    for i in range(len(solutionIDS) - 1):
        print(f"{solutionIDS[i]}  =>  {solutionIDS[i+1]}")
else:
    print("IDS: SOLUTION NOT POSSIBLE")

print("\n")

solutionUCS = UCS_3JUG()
if solutionUCS:
    print("=== UCS SOLUTION PATH ===")
    for i in range(len(solutionUCS) - 1):
        print(f"{solutionUCS[i]}  =>  {solutionUCS[i+1]}")
else:
    print("UCS: SOLUTION NOT POSSIBLE")

print("\n")

solutionGREEDY = GREEDY_3JUG()
if solutionGREEDY:
    print("=== GREEDY SOLUTION PATH ===")
    for i in range(len(solutionGREEDY) - 1):
        print(f"{solutionGREEDY[i]}  =>  {solutionGREEDY[i+1]}")
else:
    print("GREEDY: SOLUTION NOT POSSIBLE")

print("\n")

solutionAStar = A_STAR_3JUG()
if solutionAStar:
    print("=== A* SOLUTION PATH ===")
    for i in range(len(solutionAStar) - 1):
        print(f"{solutionAStar[i]}  =>  {solutionAStar[i+1]}")
else:
    print("A*: SOLUTION NOT POSSIBLE")
