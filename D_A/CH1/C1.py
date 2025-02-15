def average_followers(nums):
    if len(nums) == 0: return None
    if sum(nums) == 0: return 0
    return sum(nums) / len(nums)

def main():
    run_cases = [
    ([1], 1),
    ([1, 2, 3, 4, 5, 6, 7], 4),
    ([12, 12, 12], 12),
    ([], None),
    ]

    submit_cases = run_cases + [
        ([0], 0),
        ([100, 200, 300, 400, 500], 300),
        ([5, 10, 200, 3000, 5000], 1643),
        ([12_345, 618_222, 58_832_221, 2_180_831_475, 8_663_863_102], 2_180_831_473),
    ]
    
    correct = 0
    incorrect = 0
    for tuple in submit_cases:
        answer = average_followers(tuple[0])
        if answer == tuple[1]:
            correct += 1
            print(f"RIGHT: {answer}, CORRECT: {tuple[1]}")
        else:
            print(f"WRONG: {answer}, CORRECT: {tuple[1]}")
            incorrect += 1
    
    print(f"Correct: {correct}, Incorrect: {incorrect}")

main()