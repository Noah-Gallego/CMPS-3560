import numpy as np

np.random.seed(42)

# parameters
N = 10
M = 20
k = 3
pc = 0.50
pm = 0.10
MAX_GEN = 50

# fitness
def fitness(pop):
    return np.sum(pop, axis=1)

# tournament selection
def tournament(pop, fits):
    idx = np.random.choice(len(pop), k, replace=False)
    best = idx[np.argmax(fits[idx])]
    return pop[best].copy()

# one-point crossover at midpoint
def crossover(parent1, parent2):
    point = len(parent1) // 2
    offspring1 = np.concatenate((parent1[:point], parent2[point:]))
    offspring2 = np.concatenate((parent2[:point], parent1[point:]))
    return offspring1, offspring2

# flip one random bit
def mutate(individual):
    if np.random.rand() < pm:
        i = np.random.randint(len(individual))
        individual[i] = 1 - individual[i]
    return individual

# init population
pop = np.random.randint(0, 2, size=(N, M))

# main GA loop
for gen in range(MAX_GEN):
    fits = fitness(pop)
    print(f"gen {gen:>2}: best fitness = {fits.max()}")
    if fits.max() == M:
        print("optimal solution found")
        break

    new_pop = []
    while len(new_pop) < N:
        parent1 = tournament(pop, fits)
        parent2 = tournament(pop, fits)
        if np.random.rand() < pc:
            offspring1, offspring2 = crossover(parent1, parent2)
        else:
            offspring1, offspring2 = parent1.copy(), parent2.copy()
        offspring1 = mutate(offspring1)
        offspring2 = mutate(offspring2)
        new_pop.append(offspring1)
        new_pop.append(offspring2)
    pop = np.array(new_pop[:N])

# final result
final_fits = fitness(pop)
best = int(np.argmax(final_fits))
print(f"best chromosome: {''.join(str(b) for b in pop[best])}")
print(f"best fitness: {final_fits[best]}")
