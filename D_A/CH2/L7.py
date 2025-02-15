# logarithms
import math

def get_influencer_score(num_followers, average_engagement_percentage):
    return round(average_engagement_percentage * math.log(num_followers, 2))

def main():
    run_cases = [
        (40000, 0.3, 5), 
        (43000, 0.1, 2), 
        (100000, 0.6, 10)
        ]

    submit_cases = run_cases + [
        (1, 1, 0),
        (200, 0.8, 6),
        (300000, 0.5, 9),
        (500000, 0.2, 4),
        (750000, 0.7, 14),
        ]
    
    correct = 0
    incorrect = 0
    for tuple in submit_cases:
        answer = get_influencer_score(tuple[0], tuple[1])
        correct_answer = tuple[2]
        if answer == correct_answer:
            correct += 1
            print(f"RIGHT: {answer}, CORRECT: {correct_answer}")
        else:
            print(f"WRONG: {answer}, CORRECT: {correct_answer}")
            incorrect += 1
    
    print(f"Correct: {correct}, Incorrect: {incorrect}")

main()