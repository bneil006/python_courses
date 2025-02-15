
def toggle_case(line):
    if line.istitle():
        return line.upper() + "!!!"
    if line.isupper():
        string = line[0].upper() + line[1:].lower()
        string = string.replace("!", "")
        return string
    if len(line) > 0 and line[1:].islower():
        return line.title()
    return line

def test_user(run_cases):
    correct = 0
    incorrect = 0
    for case in run_cases:
        test = case[0]
        excepted = case[1]
        user_answer = toggle_case(test)
        if user_answer == excepted:
            correct += 1
        else:
            incorrect -= 1

    return f"CORRECT: {correct}, INCORRECT: {incorrect}"
    
def main():
    run_cases = [
    (
        "live long and prosper",
        "Live Long And Prosper",
    ),
    (
        "...Khan",
        "...KHAN!!!",
    ),
    ("BEAM ME UP, BOOTS!", "Beam me up, boots"),
    (
            "",
            "",
    ),
    (
        "I aM a DoCtOr, nOt A fUnCtIoNaL pRoGrAmMeR!!",
        "I aM a DoCtOr, nOt A fUnCtIoNaL pRoGrAmMeR!!",
    ),
    (
        "TO BOLDLY GO WHERE NO BEAR HAS GONE BEFORE!!!!",
        "To boldly go where no bear has gone before",
    ),
    (
        "Illogical",
        "ILLOGICAL!!!",
    ),
    ]

    print(test_user(run_cases))


    


main()