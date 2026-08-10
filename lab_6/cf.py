def cf_combine(cf1, cf2):
    if cf1 >= 0 and cf2 >= 0:
        return cf1 + cf2 - cf1 * cf2
    elif cf1 < 0 and cf2 < 0:
        return cf1 + cf2 + cf1 * cf2
    else:
        denom = 1 - min(abs(cf1), abs(cf2))
        if denom == 0:
            return 0.0
        return (cf1 + cf2) / denom


def get_cf(facts, name):
    for fact_name, cf in facts:
        if fact_name == name:
            return cf
    return None


def set_cf(facts, name, new_cf, use_combine=False):
    for i, (fact_name, cf) in enumerate(facts):
        if fact_name == name:
            if use_combine:
                combined = cf_combine(cf, new_cf)
                combined = round(combined, 6)
                if combined != round(cf, 6):
                    facts[i] = (fact_name, combined)
                    return True
                return False
            else:
                return False
    facts.append((name, round(new_cf, 6)))
    return True


def forward_chain(facts, rules, handle_collisions=False):
    print("=" * 60)
    print("INITIAL FACTS")
    print("=" * 60)
    for name, cf in facts:
        print(f"  {name} : {cf:.4f}")
    print()

    fired = set()
    iteration = 0
    changed = True

    while changed:
        changed = False
        iteration += 1
        print(f"--- Iteration {iteration} ---")

        for r_idx, (antecedents, consequent, cf_rule) in enumerate(rules):
            if r_idx in fired:
                continue

            ant_cfs = []
            all_present = True
            for ant in antecedents:
                cf_val = get_cf(facts, ant)
                if cf_val is None:
                    all_present = False
                    break
                ant_cfs.append(cf_val)

            if not all_present:
                continue

            min_ant_cf = min(ant_cfs)
            cf_conclusion = min_ant_cf * cf_rule

            old_cf = get_cf(facts, consequent)
            is_collision = old_cf is not None

            did_change = set_cf(
                facts, consequent, cf_conclusion,
                use_combine=(is_collision and handle_collisions)
            )

            rule_str = " AND ".join(antecedents) + f" -> {consequent}"

            if is_collision and handle_collisions and did_change:
                new_cf = get_cf(facts, consequent)
                print(f"  FIRE: {rule_str}  (CF_rule={cf_rule})")
                print(f"    min(antecedent CFs) = {min_ant_cf:.4f}")
                print(f"    computed CF = {cf_conclusion:.4f}")
                print(f"    COLLISION: old CF={old_cf:.4f}, "
                      f"new evidence={cf_conclusion:.4f} "
                      f"-> combined CF={new_cf:.4f}")
                fired.add(r_idx)
                changed = True
            elif is_collision and not handle_collisions:
                fired.add(r_idx)
                print(f"  FIRE: {rule_str}  (CF_rule={cf_rule})")
                print(f"    min(antecedent CFs) = {min_ant_cf:.4f}")
                print(f"    {consequent} already in KB with CF={old_cf:.4f}"
                      f", skipping (no collision handling)")
            elif did_change:
                new_cf = get_cf(facts, consequent)
                print(f"  FIRE: {rule_str}  (CF_rule={cf_rule})")
                print(f"    min(antecedent CFs) = {min_ant_cf:.4f}")
                print(f"    {consequent} asserted with CF = {new_cf:.4f}")
                fired.add(r_idx)
                changed = True

        if not changed:
            print("  No new facts derived.")
    print()

    print("=" * 60)
    print("FINAL FACTS")
    print("=" * 60)
    for name, cf in facts:
        print(f"  {name} : {cf:.4f}")
    print()


print("*" * 60)
print("EXAMPLE 8 - Forward Chaining with CFs")
print("*" * 60)
print()

facts_ex8 = [
    ("A", 1.00),
    ("B", 0.70),
    ("C", 0.75),
    ("D", 0.80),
    ("E", 0.50),
    ("M", -1.0),
]

rules_ex8 = [
    (("Y", "D"), "Z", 0.7),
    (("A", "B", "E"), "Y", 0.95),
    (("A",), "X", 1.0),
    (("C",), "L", 0.85),
    (("L", "M"), "N", 1.0),
]

forward_chain(facts_ex8, rules_ex8, handle_collisions=False)

facts_collision = [
    ("A", 1.00),
    ("B", 0.70),
    ("C", 0.75),
    ("D", 0.80),
    ("E", 0.50),
    ("M", -1.0),
    ("X", 0.3),
    ("Y", 0.3),
    ("Z", 0.3),
    ("L", 0.3),
    ("N", 0.3),
]

rules_collision = [
    (("Y", "D"), "Z", 0.7),
    (("A", "B", "E"), "Y", 0.95),
    (("A",), "X", 1.0),
    (("C",), "L", 0.85),
    (("L", "M"), "N", 1.0),
]

forward_chain(facts_collision, rules_collision, handle_collisions=True)