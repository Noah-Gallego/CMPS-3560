DB = ['A']
KB = [
    (['E'], 'F'), 
    (['D'], 'E'),
    (['C'], 'D'),
    (['B'], 'C'),
    (['A'], 'B')
]

count = 0
changes = True

while changes:
    changes = False
    count += 1
    print(f'Starting iteration count {count}')

    for p in KB: # For each set of rules
        antecedent, consequent = p
        print(f'Consider a rule where: {antecedent} implies: {consequent}')

        satisfied = True
        for q in antecedent:
            if q not in DB:
                satisfied = False

        if satisfied and consequent not in DB:
            DB.append(consequent)
            changes = True
            print(f'Antecedent is in DB, consequent is implied, DB is now {DB}')
        elif satisfied and consequent in DB:
            print('Consequent is implied, but was already in DB')
        else:
            print("Consequent is not implied")

print(f'No more changes! DB is: {DB}')