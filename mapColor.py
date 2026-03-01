# Map coloring problem using backtracking search.
# map as adjacency list
neighbors = {
    "WA": ["NT", "SA"],
    "NT": ["WA", "SA", "Q"],
    "SA": ["WA", "NT", "Q", "NSW", "V"],
    "Q": ["NT", "SA", "NSW"],
    "NSW": ["Q", "SA", "V"],
    "V": ["SA", "NSW"],
    "T": [],
}

colors = ["Red", "Green", "Blue"]


def is_valid(region, color, assignment):
    for n in neighbors[region]:
        if n in assignment and assignment[n] == color:
            return False
    return True


def backtrack(assignment):
    if len(assignment) == len(neighbors):
        return assignment

    # pick an unassigned region
    for region in neighbors:
        if region not in assignment:
            break

    for color in colors:
        if is_valid(region, color, assignment):
            assignment[region] = color
            result = backtrack(assignment)
            if result:
                return result
            del assignment[region]

    return None


solution = backtrack({})
print(solution)
