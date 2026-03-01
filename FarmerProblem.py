# State is (Farmer, Goat, Wolf, Cabbage)
# 0 = left bank, 1 = right bank

farmer = 0
goat = 1
wolf = 2
cabbage = 3

initialState = (0, 0, 0, 0)
goalState = (1, 1, 1, 1)


def is_safe(state):
    f, g, w, c = state

    # goat and wolf alone
    if g == w and f != g:
        return False

    # goat and cabbage alone
    if g == c and f != g:
        return False

    return True


def generate_next_state(currentState):
    f, g, w, c = currentState
    nextStates = []

    # farmer crosses alone
    nextStates.append((1 - f, g, w, c))

    # farmer takes goat
    if f == g:
        nextStates.append((1 - f, 1 - g, w, c))

    # farmer takes wolf
    if f == w:
        nextStates.append((1 - f, g, 1 - w, c))

    # farmer takes cabbage
    if f == c:
        nextStates.append((1 - f, g, w, 1 - c))

    return nextStates


def BFS(initialState, goalState):
    queue = []
    queue.append(initialState)

    visited = set()
    previous = dict()
    previous[initialState] = None

    while queue:
        current = queue.pop(0)

        if current == goalState:
            return True, previous

        visited.add(current)

        for state in generate_next_state(current):
            if state not in visited and state not in queue:
                if is_safe(state):
                    queue.append(state)
                    previous[state] = current

    return False, previous


def reconstruct_path(previous, goal):
    path = []
    while goal is not None:
        path.append(goal)
        goal = previous[goal]
    return path[::-1]

def describe(prev, curr):
    moved = [names[i] for i in range(4) if prev[i] != curr[i]]
    if len(moved) == 1:
        return "Farmer returns alone"
    else:
        return f"Farmer takes {moved[1]} across"


if __name__ == "__main__":
    answer, previous = BFS(initialState, goalState)

    if answer:
        solution = []
        path = reconstruct_path(previous, goalState)
        names = ["Farmer", "Goat", "Wolf", "Cabbage"]
        #print(path)
        
        for step in path:
            print(step)
            solution.append(step)
        
        for i in range(len(solution)-1):
            print(describe(solution[i], solution[i+1]))
        

        
    else:
        print("NO SOLUTION")