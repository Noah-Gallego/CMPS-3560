# returns fuzzy membership value for a crisp input using nearest point
def membership(inputValue, fuzzySet):
    min_distance = float('inf')
    closest_fuzzy = 0.0
    for point in fuzzySet:
        fuzzyValue, crispValue = point
        if crispValue == inputValue:
            return fuzzyValue
        distance = abs(inputValue - crispValue)
        if distance < min_distance:
            min_distance = distance
            closest_fuzzy = fuzzyValue
    return closest_fuzzy

# fuzzy sets for water (output, 0L to 2L)
none_water = ((1.0, 0.0), (0.75, 0.1), (0.50, 0.2), (0.25, 0.3), (0.0, 0.4))
bottle = ((0.0, 0.2), (0.5, 0.5), (1.0, 1.0), (0.5, 1.5), (0.0, 2.0))
alot = ((0.0, 1.0), (0.25, 1.25), (0.5, 1.50), (0.75, 1.75), (1.0, 2.0))

# fuzzy sets for temperature (input, 50F to 110F)
moderate = ((1.0, 50), (0.75, 60), (0.5, 70), (0.25, 80), (0.0, 90))
hot = ((0.0, 70), (0.25, 80), (0.5, 90), (0.75, 100), (1.0, 110))

# fuzzy sets for distance (input, 0.1 to 20 miles)
short = ((1.0, 0.1), (0.75, 1.0), (0.5, 2.0), (0.25, 3.0), (0.0, 4.0))
medium = ((0.0, 2.0), (0.5, 4.0), (1.0, 6.0), (0.5, 8.0), (0.0, 10.0))
long_dist = ((0.0, 6.0), (0.25, 8.0), (0.5, 12.0), (0.75, 16.0), (1.0, 20.0))

# test case
T = 80
L = 2

print(f"Input: Temperature = {T}F, Distance = {L} miles")
print()

# fuzzification
print("Fuzzification")
print(f"  membership({T}, moderate) = {membership(T, moderate)}")
print(f"  membership({T}, hot)      = {membership(T, hot)}")
print(f"  membership({L}, short)    = {membership(L, short)}")
print(f"  membership({L}, medium)   = {membership(L, medium)}")
print(f"  membership({L}, long)     = {membership(L, long_dist)}")
print()

# rule evaluation (AND = min, OR = max)
rule1ant = membership(L, short)
rule2ant = min(membership(T, moderate), membership(L, medium))
rule3ant = max(membership(T, hot), membership(L, long_dist))

print("Rule Evaluation")
print(f"  Rule 1 (short -> none):                rule1ant = {rule1ant}")
print(f"  Rule 2 (medium AND moderate -> bottle): rule2ant = {rule2ant}")
print(f"  Rule 3 (long OR hot -> alot):           rule3ant = {rule3ant}")
print()

# aggregation and defuzzification
numerator = 0
denominator = 0
x = 0.0
step = 0.1

print("Aggregation and Defuzzification")
print(f"  {'x':>4}  |  {'u(x)':>8}  |  {'x * u(x)':>10}")
print("  " + "-" * 35)

while x <= 2.0:
    u = (rule1ant * membership(x, none_water)
       + rule2ant * membership(x, bottle)
       + rule3ant * membership(x, alot))

    numerator += u * x
    denominator += u

    print(f"  {x:4.1f}  |  {u:8.4f}  |  {u * x:10.4f}")
    x = round(x + step, 1)

print("  " + "-" * 35)
print(f"  Sum of u(x):     {denominator:.4f}")
print(f"  Sum of x*u(x):   {numerator:.4f}")
print()

if denominator != 0:
    recommendation = numerator / denominator
    print(f"Recommendation: Bring {recommendation:.4f} liters of water.")
else:
    print("Recommendation: No water needed (denominator is 0).")
