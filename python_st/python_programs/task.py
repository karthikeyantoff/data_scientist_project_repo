# class Solution:
#     def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
#         # Step 1: Mark visited numbers
#         for num in nums:
#             index = abs(num) - 1  # Find the index corresponding to this number
#             if nums[index] > 0:   # Mark only if not already marked
#                 nums[index] = -nums[index]
        
#         # Step 2: Collect missing numbers
#         missing = []
#         for i, num in enumerate(nums):
#             if num > 0:           # Positive means not visited
#                 missing.append(i + 1)
        
#         return missing

# class Solution:
#     def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
#         l=[]
#         for i in nums:
#             i=set(i)
#             l.append(i)
#         for j in l:
#             index=abs(j)-1
#             if nums[index]>0:
#                 nums[index]=-nums[index]
            
#             m=[]
#             for k,j in enumerate(l):
#                 if k >0:
#                     m.append(k)
                
#         # Your Python code goes here
#         # Implement the logic to find all numbers that do not appear in nums.

#         return m # Placeholder, replace with your actual result

# # Test cases
# solver = Solution()

# # Test Case 1
# nums1 = [4, 3, 2, 7, 8, 2, 3, 1]
# print(f"Input: {nums1} -> Output: {solver.findDisappearedNumbers(nums1)}") # Expected: [5, 6] (order doesn't matter for output)

# # Test Case 2
# nums2 = [1, 1]
# print(f"Input: {nums2} -> Output: {solver.findDisappearedNumbers(nums2)}") # Expected: [2]

# # Test Case 3
# nums3 = [1]
# print(f"Input: {nums3} -> Output: {solver.findDisappearedNumbers(nums3)}") # Expected: []

# # Test Case 4 (More complex, edge cases)
# nums4 = [2, 2, 3, 4, 1, 5, 5, 6] # n = 8. Range [1,8]. Missing: 7, 8
# print(f"Input: {nums4} -> Output: {solver.findDisappearedNumbers(nums4)}") # Expected: [7, 8]

# # Test Case 5 (No missing numbers)
# nums5 = [1, 2, 3, 4]
# print(f"Input: {nums5} -> Output: {solver.findDisappearedNumbers(nums5)}") # Expected: []

# class Solution:
#     def rotate(self, nums: list[int], k: int) -> None:
#         n=len(nums)
#         if n==0:
#             k=k%n
#             nums[:]=nums[-k:]+nums[:-k]

# # Test cases
# solver = Solution()

# # Test Case 1
# nums1 = [1, 2, 3, 4, 5, 6, 7]
# k1 = 3
# solver.rotate(nums1, k1)
# print(f"Input: [1, 2, 3, 4, 5, 6, 7], k={k1} -> Rotated nums: {nums1}") # Expected: [5, 6, 7, 1, 2, 3, 4]

# # Test Case 2
# nums2 = [-1, -100, 3, 99]
# k2 = 2
# solver.rotate(nums2, k2)
# print(f"Input: [-1, -100, 3, 99], k={k2} -> Rotated nums: {nums2}") # Expected: [3, 99, -1, -100]

# # Test Case 3 (k larger than array length)
# nums3 = [1, 2]
# k3 = 3
# solver.rotate(nums3, k3)
# print(f"Input: [1, 2], k={k3} -> Rotated nums: {nums3}") # Expected: [2, 1] (k=3 is equivalent to k=1)

# # Test Case 4 (empty rotation)
# nums4 = [1, 2, 3]
# k4 = 0
# solver.rotate(nums4, k4)
# print(f"Input: [1, 2, 3], k={k4} -> Rotated nums: {nums4}") # Expected: [1, 2, 3]

# # Test Case 5 (rotate by full length)
# nums5 = [1, 2, 3]
# k5 = 3
# solver.rotate(nums5, k5)
# print(f"Input: [1, 2, 3], k={k5} -> Rotated nums: {nums5}") # Expected: [1, 2, 3]

# class Solution:
#     def rotate(self, nums: list[int], k: int) -> None:
#        n=len(nums)# Replace this with your actual implementation
#        if n==0 or n==1 or k%n==0:
#            return -1
#        k=k%n
#        def rev(nn,s,e):
#           while s<e:
#             nn[s],nn[e]=nn[e],nn[s]
#             s+=1
#             e-=1
#        rev(nums,0,n-1)
#        rev(nums,0,k-1)
#        rev(nums,k,n-1)
# # Test cases (same as before, but expecting O(1) space implementation)
# solver = Solution()

# nums1 = [1, 2, 3, 4, 5, 6, 7]
# k1 = 3
# solver.rotate(nums1, k1)
# print(f"Input: [1, 2, 3, 4, 5, 6, 7], k={k1} -> Rotated nums: {nums1}") # Expected: [5, 6, 7, 1, 2, 3, 4]

# nums2 = [-1, -100, 3, 99]
# k2 = 2
# solver.rotate(nums2, k2)
# print(f"Input: [-1, -100, 3, 99], k={k2} -> Rotated nums: {nums2}") # Expected: [3, 99, -1, -100]

# nums3 = [1, 2]
# k3 = 3
# solver.rotate(nums3, k3)
# print(f"Input: [1, 2], k={k3} -> Rotated nums: {nums3}") # Expected: [2, 1]

# nums4 = [1, 2, 3]
# k4 = 0
# solver.rotate(nums4, k4)
# print(f"Input: [1, 2, 3], k={k4} -> Rotated nums: {nums4}") # Expected: [1, 2, 3]

# nums5 = [1, 2, 3]
# k5 = 3
# solver.rotate(nums5, k5)
# print(f"Input: [1, 2, 3], k={k5} -> Rotated nums: {nums5}") # Expected: [1, 2, 3]

# nums6 = list(range(1, 11)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# k6 = 27
# solver.rotate(nums6, k6)
# print(f"Input: [1..10], k={k6} -> Rotated nums: {nums6}") # Expected: [4, 5, 6, 7, 8, 9, 10, 1, 2, 3]

def find_pair_sum(arr, target_sum):
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target_sum:
            return True # Found a pair
        elif current_sum < target_sum:
            left += 1 # Need a larger sum, move left pointer right
        else: # current_sum > target_sum
            right -= 1 # Need a smaller sum, move right pointer left
            
    return False # No pair found

# Example usage:
print(find_pair_sum([1, 2, 3, 4, 5], 7)) # Output: True (2+5, 3+4)
print(find_pair_sum([1, 2, 3, 4, 5], 10)) # Output: False
print(find_pair_sum([1, 2, 3, 4, 5], 3)) # Output: True (1+2)