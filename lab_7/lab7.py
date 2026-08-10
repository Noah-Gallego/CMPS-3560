# Water (Output) - 0L to 2L
none_water = ((1.0, 0), (0.75, 0.1), (0.50, 0.2), (0.25, 0.3), (0.0, 0.4))
bottle = ((0.0, 0.2), (0.5, 0.5), (1.0, 1.0), (0.5, 1.5), (0.0, 2.0))
alot = ((0.0, 1.0), (0.25, 1.25), (0.5, 1.5), (0.75, 1.75), (1.0, 2.0))

# Temperature (Input) - 32F to 120F
moderate = ((1.0, 50), (0.75, 60), (0.5, 70), (0.25, 80), (0.0, 90))
hot = ((0.0, 70), (0.25, 80), (0.5, 90), (0.75, 100), (1.0, 110))

# Distance (Input) - 0.25 to 20 miles
short = ((1.0, 0.1), (0.75, 1.0), (0.5, 2.0), (0.25, 3.0), (0.0, 4.0))
medium = ((0.0, 2.0), (0.5, 4.0), (1.0, 6.0), (0.5, 8.0), (0.0, 10.0))
long = ((0.0, 6.0), (0.25, 8.0), (0.5, 12.0), (0.75, 16.0), (1.0, 20.0))


# Returns fuzzy membership value for a crisp input (nearest match)
def membership(inputValue, fuzzySet):
    minDist = float('inf')
    result = None
    for fuzzyValue, crisp in fuzzySet:
        dist = abs(inputValue - crisp)
        if dist < minDist:
            minDist = dist
            result = fuzzyValue
    return result


# Returns crisp value for a fuzzy membership input (nearest match)
def inverseMembership(inputFuzzy, fuzzySet):
    minDist = float('inf')
    result = None
    for fuzzyValue, crisp in fuzzySet:
        dist = abs(inputFuzzy - fuzzyValue)
        if dist < minDist:
            minDist = dist
            result = crisp
    return result


# Test membership()
print("membership() tests")
print(f"  membership(-3, bottle)          = {membership(-3, bottle)}")
print(f"  membership(1.0, bottle)         = {membership(1.0, bottle)}")
print(f"  membership(0.3, bottle)         = {membership(0.3, bottle)}")
print(f"  membership(0.712321345, bottle) = {membership(0.712321345, bottle)}")
print(f"  membership(10000, bottle)       = {membership(10000, bottle)}")
print(f"  membership(2.0, bottle)         = {membership(2.0, bottle)}")
print(f"  membership(1.3, bottle)         = {membership(1.3, bottle)}")
print()

# Test inverseMembership()
print("inverseMembership() tests")
print(f"  inverseMembership(0.0, bottle) = {inverseMembership(0.0, bottle)}")
print(f"  inverseMembership(0.2, bottle) = {inverseMembership(0.2, bottle)}")
print(f"  inverseMembership(0.5, bottle) = {inverseMembership(0.5, bottle)}")
print(f"  inverseMembership(0.8, bottle) = {inverseMembership(0.8, bottle)}")
print(f"  inverseMembership(1.0, bottle) = {inverseMembership(1.0, bottle)}")
print()

# Rule 1: IF distance is short THEN water is none
print("Rule Evaluations")
print("-" * 40)

km = 0.1
fuzzyDistance = membership(km, short)
crispOutput = inverseMembership(fuzzyDistance, none_water)
print(f"Rule 1 (dist={km}km): short -> none")
print(f"  membership={fuzzyDistance}, water={crispOutput}L")
print()

km = 2.4
fuzzyDistance = membership(km, short)
crispOutput = inverseMembership(fuzzyDistance, none_water)
print(f"Rule 1 (dist={km}km): short -> none")
print(f"  membership={fuzzyDistance}, water={crispOutput}L")
print()

# Rule 2: IF distance is medium OR temp is moderate THEN water is bottle
km = 5.0
temp = 65
fuzzyDistance = membership(km, medium)
fuzzyTemp = membership(temp, moderate)
premiseFuzzy = max(fuzzyDistance, fuzzyTemp)
crispOutput = inverseMembership(premiseFuzzy, bottle)
print(f"Rule 2 (dist={km}km, temp={temp}F): medium OR moderate -> bottle")
print(f"  dist={fuzzyDistance}, temp={fuzzyTemp}, OR={premiseFuzzy}, water={crispOutput}L")
print()

# Rule 3: IF distance is long OR temp is hot THEN water is a lot
km = 3
temp = 80
fuzzyDistance = membership(km, long)
fuzzyTemp = membership(temp, hot)
premiseFuzzy = max(fuzzyDistance, fuzzyTemp)
crispOutput = inverseMembership(premiseFuzzy, alot)
print(f"Rule 3 (dist={km}km, temp={temp}F): long OR hot -> alot")
print(f"  dist={fuzzyDistance}, temp={fuzzyTemp}, OR={premiseFuzzy}, water={crispOutput}L")
print()

# Rule (AND): IF distance is long AND temp is hot THEN water is a lot
km = 15
temp = 100
fuzzyDistance = membership(km, long)
fuzzyTemp = membership(temp, hot)
premiseFuzzy = min(fuzzyDistance, fuzzyTemp)
crispOutput = inverseMembership(premiseFuzzy, alot)
print(f"Rule AND (dist={km}km, temp={temp}F): long AND hot -> alot")
print(f"  dist={fuzzyDistance}, temp={fuzzyTemp}, AND={premiseFuzzy}, water={crispOutput}L")
