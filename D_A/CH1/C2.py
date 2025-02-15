def median_followers(nums):
    if len(nums) == 0:
        return None
    nums = sorted(nums)
    n = len(nums)
    if n % 2 == 0:
        return (nums[n // 2 - 1] + nums[n // 2]) / 2
    return nums[n // 2]

def main():
    run_cases = [
        ([12, 12, 12], 12),
        ([10, 200, 3000, 5000, 4], 200),
        ([7, 4, 3, 100, 2343243, 343434, 1, 2, 32], 7),
        ([], None),
    ]

    submit_cases = run_cases + [
        ([0], 0),
        ([1000000], 1000000),
        ([5, 2, 3, 7, 6, 4], 4.5),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5.5),
    ]
    
    correct = 0
    incorrect = 0
    for tuple in submit_cases:
        answer = median_followers(tuple[0])
        if answer == tuple[1]:
            correct += 1
            print(f"RIGHT: {answer}, CORRECT: {tuple[1]}")
        else:
            print(f"WRONG: {answer}, CORRECT: {tuple[1]}")
            incorrect += 1
    
    print(f"Correct: {correct}, Incorrect: {incorrect}")

main()