# TwoSums
def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return print([])

n = int(input("Enter the number of integers: "))  # n is the length of the array

A = [int(input("Enter an integer: ")) for i in range(n)]

B = int(input("enter the target value:"))

twoSum(A , B)
