KB = [
    (["Y", "D"], "Z"),
    (["X", "B", "E"], "Y"),
    (["A"], "X"),
    (["C"], "L"),
    (["L", "M"], "N")
]

DB = {"A", "B", "C", "D", "E"}

goal = "Z"

def PL_BC(goal, KB, DB):
    if goal in DB:
        return True
    
    for c in range(len(KB)):
        antecedent, consequent = KB[c]
        if consequent == goal:
            implied = True
            for literal in antecedent:
                if not PL_BC(literal, KB, DB):
                    implied = False
                    break
                if implied:
                    return True
    return False
    

print(PL_BC(goal, KB, DB))