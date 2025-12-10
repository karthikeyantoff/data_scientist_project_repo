# class Solution:
#     def longestOnes(self, nums: list[int], k: int) -> int:
        
# # Test cases
# solver = Solution()

# # Test Case 1
# nums1 = [1, 1, 0, 0, 1, 1, 1, 0, 1, 1]
# k1 = 2
# print(f"Input: nums={nums1}, k={k1} -> Output: {solver.longestOnes(nums1, k1)}") # Expected: 6

# # Test Case 2
# nums2 = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
# k2 = 3
# print(f"Input: nums={nums2}, k={k2} -> Output: {solver.longestOnes(nums2, k2)}") # Expected: 10

# # Test Case 3 (No zeros, k doesn't matter)
# nums3 = [1, 1, 1, 1, 1]
# k3 = 0
# print(f"Input: nums={nums3}, k={k3} -> Output: {solver.longestOnes(nums3, k3)}") # Expected: 5

# # Test Case 4 (All zeros, k = 0)
# nums4 = [0, 0, 0, 0, 0]
# k4 = 0
# print(f"Input: nums={nums4}, k={k4} -> Output: {solver.longestOnes(nums4, k4)}") # Expected: 0

# # Test Case 5 (All zeros, k large enough to flip all)
# nums5 = [0, 0, 0, 0, 0]
# k5 = 3
# print(f"Input: nums={nums5}, k={k5} -> Output: {solver.longestOnes(nums5, k5)}") # Expected: 5

# # Test Case 6 (k allows flipping all zeros in a long stretch)
# nums6 = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
# k6 = 5
# print(f"Input: nums={nums6}, k={k6} -> Output: {solver.longestOnes(nums6, k6)}") # Expected: 11

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         seen={}
#         for i in range(len(nums)):
#             # overall_cubles_sum=nums[i]
#             find_best_cuble=target-nums[i]
#             if find_best_cuble in seen:
#                 cuble_index=seen[find_best_cuble] 
#                 return [cuble_index,i]
#             seen[nums[i]]=i

# s = "madam"
# left = 0
# right = len(s) - 1
# is_palindrome = True

# while left < right:
#     if s[left] != s[right]:
#         is_palindrome = False
#         break
#     left += 1
#     right -= 1

# print("Palindrome" if is_palindrome else "Not Palindrome")

# l=[1,2,3,0,5,0,7]
# result=[]
# n=len(l)
# left=0
# right=n-1
# while left<right:
# for i in range(len(l)):
#     if left==0:
#         temp=left
#         left=i
#         result.append(left)
#         left+1
# print(result)


# def k(nums):
#     n=sorted(nums)
#     print(n)
#     if n==0:
#         return 0
#     # l=[n[0]]
#     # l=1
#     for i in range(len(n)-1):
#         # if n[i+1]==n[i]:
#         #     continue
#         if n[i+1]-n[i]==1:
#             # l.append(n[i])
#             l.append(n[i+1])
#             # l+=1
#     return len(l)  
#         # else:
#         #     return False
# l=[]
# print(k(l))

def longestOnes(nums,k):
    # currlength=0
    for i in range(len(nums)):
        if nums[i]==0 and k!=0:
            nums[i]=1
            k-=1
            print(nums)
numss=[1,1,1,0,0,0,1,1,1,1,0]
kk=2
longestOnes(numss,kk)

