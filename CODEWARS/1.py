# Your task is to make a function that can take any non-negative integer 
# as an argument and return it with its digits in descending order. 
# Essentially, rearrange the digits to create the highest possible number.
def descending_order(num):
    largest_number = ""
    
    numbers = []
    num = str(num)
    for i in num:
        numbers.append(int(i))
    
    length = len(numbers)
    while length > 0:
        highest = float("-inf")
        for i in numbers:
            if i > highest:
                highest = i
        largest_number += str(highest)
        numbers.remove(highest)
        length -= 1

    return int(largest_number)

def main():
    print(descending_order(87945))

main()