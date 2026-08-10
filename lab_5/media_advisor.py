KB = []

for env in ["papers", "manuals", "documents", "textbooks"]:
    KB.append(([env], "verbal"))
for env in ["pictures", "illustrations", "photographs", "diagrams"]:
    KB.append(([env], "visual"))
for env in ["machines", "buildings_env", "tools"]:
    KB.append(([env], "physical_object"))
for env in ["numbers", "formulas", "computer_programs"]:
    KB.append(([env], "symbolic"))
for job in ["lecturing", "advising", "counselling"]:
    KB.append(([job], "oral"))
for job in ["building_job", "repairing", "troubleshooting"]:
    KB.append(([job], "hands_on"))
for job in ["writing", "typing", "drawing"]:
    KB.append(([job], "documented"))
for job in ["evaluating", "reasoning", "investigating"]:
    KB.append(([job], "analytical"))

KB.append((["physical_object", "hands_on", "feedback_required"], "workshop"))
KB.append((["symbolic", "analytical", "feedback_required"], "lecture_tutorial"))
KB.append((["visual", "documented", "feedback_not_required"], "videocassette"))
KB.append((["visual", "oral", "feedback_required"], "lecture_tutorial"))
KB.append((["verbal", "analytical", "feedback_required"], "lecture_tutorial"))
KB.append((["verbal", "oral", "feedback_required"], "role_play_exercises"))

MEDIA_GOALS = ["workshop", "lecture_tutorial", "videocassette", "role_play_exercises"]


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


def run_advisor(DB):
    print(f"Facts: {DB}")
    for media in MEDIA_GOALS:
        result = PL_BC(media, KB, DB)
        status = "RECOMMENDED" if result else "not recommended"
        print(f"  {media}: {status}")
    print()


print("Test 1: machines, repairing, feedback_required")
DB = set()
DB.add("machines")
DB.add("repairing")
DB.add("feedback_required")
run_advisor(DB)

print("Test 2: pictures, writing, feedback_not_required")
DB = set()
DB.add("pictures")
DB.add("writing")
DB.add("feedback_not_required")
run_advisor(DB)

print("Test 3: textbooks, advising, feedback_required")
DB = set()
DB.add("textbooks")
DB.add("advising")
DB.add("feedback_required")
run_advisor(DB)

print("Test 4: formulas, evaluating, feedback_required")
DB = set()
DB.add("formulas")
DB.add("evaluating")
DB.add("feedback_required")
run_advisor(DB)