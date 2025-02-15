def sum(nums):
    sum = 0
    if nums == None:
        return 0
        
    for i in nums:
        sum += i
    return sum

def main():
    run_cases = [
        ([7, 4, 3, 100, 2343243, 343434, 1, 2, 32], 2686826), 
        ([12, 12, 12], 36)
        ]
    submit_cases = run_cases + [
        ([10, 200, 3000, 5000, 4], 8214),
        ([], 0),
        ([1], 1),
        ([123456789], 123456789),
        ([-1, -2, -3], -6),
        ([0, 0, 0, 0, 0], 0),
        ]
    
    correct = 0
    incorrect = 0
    for tuple in submit_cases:
        if sum(tuple[0]) == tuple[1]:
            correct += 1
        else:
            incorrect += 1
            print(f"Incorrect answer: {tuple[0]}, should be: {tuple[1]}")
    
    print(f"Correct: {correct}, Incorrect: {incorrect}")
            

main()