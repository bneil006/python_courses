# exponents and spread
def get_estimated_spread(audiences_followers):
    num_followers = len(audiences_followers)
    if num_followers == 0: return 0
    average = sum(audiences_followers) / num_followers
    return round(average * (num_followers ** 1.2))

def main():
    run_cases = [
        ([7, 4, 3, 100, 765, 2344, 1, 2, 32], 5056),
        ([12, 12, 12], 45),
        ([10, 200, 3000, 5000, 4], 11333),
    ]

    submit_cases = run_cases + [
        ([], 0),
        ([1, 1, 1], 4),
        ([100], 100),
        ([50, 60, 70, 80, 90], 483),
        ([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 872),
        ([5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100], 1912),
    ]
    
    correct = 0
    incorrect = 0
    for tuple in submit_cases:
        answer = get_estimated_spread(tuple[0])
        if answer == tuple[1]:
            correct += 1
            print(f"RIGHT: {answer}, CORRECT: {tuple[1]}")
        else:
            print(f"WRONG: {answer}, CORRECT: {tuple[1]}")
            incorrect += 1
    
    print(f"Correct: {correct}, Incorrect: {incorrect}")

main()