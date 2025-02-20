# Merge Sort
import time

def merge_sort(nums):
    if len(nums) < 2: return nums
    left_split = merge_sort(nums[:len(nums) // 2]) # nums[:ENDING AT] only need to return all leftmost numbers to index
    right_split = merge_sort(nums[len(nums) // 2:]) # nums[STARTING AT:] only need to return all rightmost numbers from index
    return merge(left_split, right_split)


def merge(first, second):
    final = []
    i, j = 0, 0 # going to use these to increment our index
    while i < len(first) and j < len(second):
        if first[i] <= second[j]: # which is smallest OR EQUAL, whichever is add that indexed item to the final list and increment the index then repeate
            final.append(first[i])
            i += 1
        else:
            final.append(second[j])
            j += 1
    
    while i < len(first): # add the remaining of the first list to final
        final.append(first[i])
        i += 1
    
    while j < len(second): # add the remaining of the second list to final
        final.append(second[j])
        j += 1

    return final




run_cases = [([3, 2, 1], [1, 2, 3]), ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5])]

submit_cases = run_cases + [
    ([], []),
    ([7], [7]),
    ([4, -7, 1, 0, 5], [-7, 0, 1, 4, 5]),
    ([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([1, 1, 1, 1, 1], [1, 1, 1, 1, 1]),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input: {input1}")
    print(f"Expecting: {expected_output}")
    start = time.time()
    result = merge_sort(input1)
    end = time.time()
    timeout = 1.00
    if (end - start) < timeout:
        print(f"test completed in less than {timeout * 1000} milliseconds!")
        if result == expected_output:
            print(f"Actual: {result}")
            print("Pass")
            return True
        print(f"Actual: {result}")
        print("Fail")
        return False
    else:
        print(f"test took longer than {timeout * 1000} milliseconds!")
        print(f"Actual: {result}")
        print("Fail")
        return False


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()