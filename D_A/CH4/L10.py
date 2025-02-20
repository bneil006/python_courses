# Insertion Sort
import time

def insertion_sort(nums):
    for i in range(0, len(nums)):
        j = i
        while j > 0 and nums[j-1] > nums[j]: # only want this running when nums[j-1] and nums[j] need to swap and nums[j] is greater than index 0 in the list
            nums[j-1], nums[j] = nums[j], nums[j-1] # swapping elements to put them in order
            j -= 1 # decrementing to the next index element and checking again
    return nums


run_cases = [([4, 3, 2, 1], [1, 2, 3, 4]), ([9, 5, -3, 7], [-3, 5, 7, 9])]

submit_cases = run_cases + [
    ([], []),
    ([1], [1]),
    ([5, 3, 4, 1, 2], [1, 2, 3, 4, 5]),
    ([0, -2, -5, 3, 2, 1], [-5, -2, 0, 1, 2, 3]),
    ([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    print(f"Expecting: {expected_output}")
    start = time.time()
    result = insertion_sort(input1)
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