# factorials
def num_possible_orders(num_posts):
    if num_posts < 0: return None
    if num_posts == 0: return 1
    result = 1
    for i in range(1, num_posts + 1):
        result *= i
    return result

def main():

    run_cases = [(2, 2), (3, 6), (5, 120)]

    submit_cases = run_cases + [
        (1, 1),
        (6, 720),
        (7, 5040),
        (8, 40320),
        (9, 362880),
        (11, 39916800),
        ]
    
    correct = 0
    incorrect = 0
    for tuple in submit_cases:
        answer = num_possible_orders(tuple[0])
        correct_answer = tuple[1]
        if answer == correct_answer:
            correct += 1
            print(f"RIGHT: {answer}, CORRECT: {correct_answer}")
        else:
            print(f"WRONG: {answer}, CORRECT: {correct_answer}")
            incorrect += 1
    
    print(f"Correct: {correct}, Incorrect: {incorrect}")

main()