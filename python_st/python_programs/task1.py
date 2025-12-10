# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         left,right=0,len(s)-1
#         while left<right:
#             while left<right and not s[left].isalnum():
#                 left+=1
#             while left<right and not s[right].isalnum():
#                 right-=1
#             if s[left].lower()!=s[right].lower():
#                 return False
#             left+=1
#             right-=1
#         return True
#          # Placeholder, replace with your actual result

# # Test cases
# solver = Solution()

# # Test Case 1
# s1 = "A man, a plan, a canal: Panama"
# print(f"Input: '{s1}' -> Output: {solver.isPalindrome(s1)}") # Expected: True

# # Test Case 2
# s2 = "race a car"
# print(f"Input: '{s2}' -> Output: {solver.isPalindrome(s2)}") # Expected: False

# # Test Case 3
# s3 = " "
# print(f"Input: '{s3}' -> Output: {solver.isPalindrome(s3)}") # Expected: True

# # Test Case 4 (Empty string)
# s4 = ""
# print(f"Input: '{s4}' -> Output: {solver.isPalindrome(s4)}") # Expected: True

# # Test Case 5 (Single character)
# s5 = "a"
# print(f"Input: '{s5}' -> Output: {solver.isPalindrome(s5)}") # Expected: True

# # Test Case 6 (Non-alphanumeric characters only)
# s6 = ",,,"
# print(f"Input: '{s6}' -> Output: {solver.isPalindrome(s6)}") # Expected: True (becomes empty string)

# # Test Case 7 (Numbers)
# s7 = "0P"
# print(f"Input: '{s7}' -> Output: {solver.isPalindrome(s7)}") # Expected: False (0 != p)

# # Test Case 8 (Mixed numbers and letters)
# s8 = "A1B22B1A"
# print(f"Input: '{s8}' -> Output: {solver.isPalindrome(s8)}") # Expected: True