# geometric sequence
def get_follower_prediction(follower_count, influencer_type, num_months):
    n = 2
    if influencer_type == "fitness": n = 4
    if influencer_type == "cosmetic": n = 3
    return follower_count * (n**num_months)

def main():
    run_cases = [
        (10, "fitness", 1, 40),
        (10, "fitness", 2, 160),
        (12, "cosmetic", 4, 972),
    ]

    submit_cases = run_cases + [
        (15, "business", 4, 240),
        (10, "fitness", 5, 10240),
        (10, "fitness", 6, 40960),
        (10, "fitness", 7, 163840),
        (10, "fitness", 8, 655360),
        (10, "tech", 9, 5120),
    ]
    
    correct = 0
    incorrect = 0
    for tuple in submit_cases:
        answer = get_follower_prediction(tuple[0], tuple[1], tuple[2])
        correct_answer = tuple[3]
        if answer == correct_answer:
            correct += 1
            print(f"RIGHT: {answer}, CORRECT: {correct_answer}")
        else:
            print(f"WRONG: {answer}, CORRECT: {correct_answer}")
            incorrect += 1
    
    print(f"Correct: {correct}, Incorrect: {incorrect}")

main()