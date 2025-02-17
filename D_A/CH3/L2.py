# O(n) - Order 'n'

def find_max(nums):
    max = float("-inf")
    for n in nums:
        if n > max:
            max = n
    return max
        
def main():

    run_cases = [([7, 4, 3, 100, 2343243, 343434, 1, 2, 32], 2343243), ([12, 12, 12], 12)]

    submit_cases = run_cases + [
        ([10, 200, 3000, 5000, 4], 5000),
        ([0], 0),
        ([-1, -2, -3], -1),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10),
        ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 10),
    ]
    
    correct = 0
    incorrect = 0
    for tuple in submit_cases:
        answer = find_max(tuple[0])
        correct_answer = tuple[1]
        if answer == correct_answer:
            correct += 1
            print(f"RIGHT: {answer}, CORRECT: {correct_answer}")
        else:
            print(f"WRONG: {answer}, CORRECT: {correct_answer}")
            incorrect += 1
    
    print(f"Correct: {correct}, Incorrect: {incorrect}")

main()