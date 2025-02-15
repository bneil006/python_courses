# exponential decay
def decayed_followers(intl_followers, fraction_lost_daily, days):
    res = intl_followers * (1 - fraction_lost_daily) ** days
    return round(res)

        
def main():

    run_cases = [
        (200, 0.5, 1, 100),
        (200, 0.5, 2, 50),
        (200, 0.05, 3, 171),
    ]

    submit_cases = run_cases + [
        (1000, 0.005, 2, 990),
        (1000, 0.05, 3, 857),
        (1200, 0.55, 8, 2),
        (1200, 0.09, 16, 265),
        (0, 0.5, 1, 0),
        (100, 0, 5, 100),
    ]
    
    correct = 0
    incorrect = 0
    for tuple in submit_cases:
        answer = decayed_followers(tuple[0], tuple[1], tuple[2])
        correct_answer = tuple[3]
        if answer == correct_answer:
            correct += 1
            print(f"RIGHT: {answer}, CORRECT: {correct_answer}")
        else:
            print(f"WRONG: {answer}, CORRECT: {correct_answer}")
            incorrect += 1
    
    print(f"Correct: {correct}, Incorrect: {incorrect}")

main()