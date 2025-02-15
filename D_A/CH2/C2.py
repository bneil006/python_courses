# exponential decay
import math

def log_scale(data, base):
    return_list = []
    for i in data:
        return_list.append(round(math.log(i, base)))
    return return_list
        
def main():

    run_cases = [
        ([1, 10, 100, 1000], 10, [0.0, 1.0, 2.0, 3.0]),
        ([1, 2, 4, 8], 2, [0.0, 1.0, 2.0, 3.0]),
    ]

    submit_cases = run_cases + [
        ([2, 4, 8, 16], 2, [1.0, 2.0, 3.0, 4.0]),
        ([3, 9, 27, 81], 3, [1.0, 2.0, 3.0, 4.0]),
        ([5, 25, 125, 625], 5, [1.0, 2.0, 3.0, 4.0]),
        ([10, 100, 1000, 10000], 10, [1.0, 2.0, 3.0, 4.0]),
        ([20, 400, 8000, 160000], 20, [1.0, 2.0, 3.0, 4.0]),
    ]
    
    correct = 0
    incorrect = 0
    for tuple in submit_cases:
        answer = log_scale(tuple[0], tuple[1])
        correct_answer = tuple[2]
        if answer == correct_answer:
            correct += 1
            print(f"RIGHT: {answer}, CORRECT: {correct_answer}")
        else:
            print(f"WRONG: {answer}, CORRECT: {correct_answer}")
            incorrect += 1
    
    print(f"Correct: {correct}, Incorrect: {incorrect}")

main()