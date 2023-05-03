# Longest Substring without repeating characters
def lengthOfLongestSubstring(s):
    seen = {}
    start = 0
    max_len = 0
    
    for i, char in enumerate(s):
        if char in seen and seen[char] >= start:
            start = seen[char] + 1
        seen[char] = i
        max_len = max(max_len, i - start + 1)
    
    return print(max_len)
A = input("Enter a string:")

lengthOfLongestSubstring(A)