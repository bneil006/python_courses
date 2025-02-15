def find_minimum(nums):
    minimum = float("inf")

    if len(nums) == 0: return None
    if type(nums) != list: raise Exception("Not an integer")

    for i in nums:
        if i < minimum:
            minimum = i
    return minimum

def main():
    run_cases = [
        ([7, 4, 3, 100, 2343243, 343434, 1, 2, 32], 1),
        ([12, 12, 12], 12),
        ([10, 200, 3000, 5000, 4], 4),
        ]

    submit_cases = run_cases + [
        ([1], 1),
        ([1, 2, 3, 4, 5], 1),
        ([5, 4, 3, 2, 1], 1),
        ([100, 200, 300, 400, 500], 100),
        ([500, 400, 300, 200, 100], 100),
        ([], None),
        ]
    
    correct = 0
    incorrect = 0
    for tuple in submit_cases:
        if find_minimum(tuple[0]) == tuple[1]:
            correct += 1
        else:
            incorrect += 1
            print(f"Incorrect answer: {tuple[0]}, should be: {tuple[1]}")
    
    print(f"Correct: {correct}, Incorrect: {incorrect}")

main()