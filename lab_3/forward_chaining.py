KB = [
    (["A","B","C"],"D"),
    (["E"],"F"),
    (["M","N"],"P")
]
DB = ["E","M","A","B","C"]
q = "D"
count = [3,1,2]
inferred = []

entailed = False
iteration = 0

while DB:
    iteration += 1
    print(f"Start iteration {iteration}")
    p = DB.pop(0)
    if p == q:
        print("Goal is entailed!")
        entailed = True
        break
    if p not in inferred:
        inferred.append(p)
        for c in range(len(KB)):
            antecedent, consequent = KB[c]
            if p in antecedent:
                count[c] -= 1
                if count[c] == 0:
                    DB.append(consequent)
    print(f"At the end of iteration {iteration}, we have DB={DB}")
if not entailed:
    print("Goal is not entailed")